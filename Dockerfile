# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables to avoid Python buffering and prompt
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Set working directory
WORKDIR /app

# Install system dependencies for Playwright and OCR
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    gnupg \
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

# Copy your code into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Playwright browsers (Chromium, Firefox, WebKit) and dependencies
RUN pip install playwright
RUN playwright install --with-deps

# Expose port (adjust if you run on a different port)
EXPOSE 8000

# Command to start your FastAPI server (update if your entry point is different)
CMD ["uvicorn", "api.research:app", "--host", "0.0.0.0", "--port", "8000"]
