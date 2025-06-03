FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/serpapi/serpapi-python.git

EXPOSE 8000

CMD ["uvicorn", "api.research:app", "--host", "0.0.0.0", "--port", "8000"]
