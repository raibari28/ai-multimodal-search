export async function POST(req) {
  const body = await req.json();

  return Response.json({
    query: body.query,
    results: ["ok"]
  });
}

export async function GET() {
  return Response.json({ status: "ok" });
}
