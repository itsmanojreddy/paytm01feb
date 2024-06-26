# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required system packages
RUN apt-get update \
    && apt-get install -y \
        wget \
        unzip \
        chromium \
    && rm -rf /var/lib/apt/lists/*

# Install chromedriver for Chrome
RUN wget -q "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/linux64/chrome-linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Set up Python environment
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy test files
COPY . /app/

# Run pytest with specific markers when the container starts
CMD ["python3", "-m","pytest", "-m", "test123","--html=reportss.html","--capture","sys"]



# --html=reportss.html --capture sys
