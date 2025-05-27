# FastAPI Dockerized App

## Run locally

```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

Then test:

```bash
curl -X POST http://localhost:8000/search \
-H "Content-Type: application/json" \
-d '{"query": "hello"}'
```
