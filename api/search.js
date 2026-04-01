export default function handler(req, res) {
  if (req.method === "POST") {
    const { query } = req.body || {};

    return res.status(200).json({
      query,
      results: ["ok"]
    });
  }

  return res.status(200).json({ status: "ok" });
}
