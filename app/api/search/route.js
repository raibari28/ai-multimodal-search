import { multimodalSearch } from "@/app/lib/searchEngine";

export async function POST(req) {
  const body = await req.json();

  const results = multimodalSearch(body.query, body.type);

  return Response.json({
    query: body.query,
    results
  });
}

export async function GET() {
  return Response.json({ status: "search endpoint ready" });
}
