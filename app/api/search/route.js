import { getEmbedding } from "@/app/lib/embeddings";
import { searchVector } from "@/app/lib/vectorStore";

export async function POST(req) {
  const body = await req.json();

  const queryVec = await getEmbedding(body.query);
  const results = searchVector(queryVec);

  return Response.json({
    query: body.query,
    results
  });
}
