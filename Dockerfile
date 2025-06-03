FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything to the container
COPY . /app

# Install system dependencies (add more as needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libgtk-3-0 \
    libx11-xcb1 \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# If you need Playwright browsers:
RUN pip install playwright
RUN playwright install --with-deps

# Expose the FastAPI port
EXPOSE 8000

# Start FastAPI with uvicorn (Linux style, NOT Windows "cmd")
CMD ["uvicorn", "api.research:app", "--host", "0.0.0.0", "--port", "8000"]
