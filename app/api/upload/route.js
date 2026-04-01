export const runtime = "nodejs";

import pdf from "pdf-parse";
import mammoth from "mammoth";
import * as XLSX from "xlsx";

import { getEmbedding } from "@/app/lib/embeddings";
import { addVector } from "@/app/lib/vectorStore";

export async function POST(req) {
  const formData = await req.formData();
  const file = formData.get("file");

  const buffer = Buffer.from(await file.arrayBuffer());
  const filename = file.name.toLowerCase();

  let text = "";

  // 🔍 extract content
  if (filename.endsWith(".pdf")) {
    const data = await pdf(buffer);
    text = data.text;
  } else if (filename.endsWith(".docx")) {
    const data = await mammoth.extractRawText({ buffer });
    text = data.value;
  } else if (filename.endsWith(".xlsx")) {
    const workbook = XLSX.read(buffer, { type: "buffer" });
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    text = XLSX.utils.sheet_to_csv(sheet);
  } else {
    return Response.json({ error: "Unsupported file" });
  }

  // 🔥 THIS IS THE NEW PART
  const embedding = await getEmbedding(text);

  addVector(embedding, {
    filename,
    preview: text.slice(0, 200)
  });

  return Response.json({
    status: "indexed",
    filename
  });
}
