import json

def handler(request):
    if request.method == "POST":
        body = json.loads(request.body)

        query = body.get("query", "")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "query": query,
                "results": ["ok"]
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"status": "ok"})
    }
