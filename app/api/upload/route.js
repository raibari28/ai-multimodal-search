import pdf from "pdf-parse";
import mammoth from "mammoth";
import * as XLSX from "xlsx";

export async function POST(req) {
  const formData = await req.formData();
  const file = formData.get("file");

  if (!file) {
    return Response.json({ error: "No file uploaded" }, { status: 400 });
  }

  const buffer = Buffer.from(await file.arrayBuffer());
  const filename = file.name.toLowerCase();

  let text = "";

  try {
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
    } else if (filename.match(/\.(jpg|png|gif)$/)) {
      text = "Image uploaded (processing placeholder)";
    } else {
      return Response.json({ error: "Unsupported file type" }, { status: 400 });
    }

    return Response.json({
      filename,
      preview: text.slice(0, 500)
    });

  } catch (err) {
    return Response.json({ error: "Processing failed" }, { status: 500 });
  }
}
