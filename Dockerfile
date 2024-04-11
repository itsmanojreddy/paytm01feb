# Use an official Python runtime as the base image
FROM python:3.9-slim
FROM alpine:latest

RUN apk update && apk add chromium chromium-chromedriver

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install any necessary dependencies for ChromeDriver
RUN apt-get update \
    && apt-get install -y wget unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the ChromeDriver version you want to use
ARG CHROME_DRIVER_VERSION="123.0.6312.106"

# Download and install ChromeDriver
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/bin/chromedriver


# Set the PATH environment variable to include the directory containing ChromeDriver
ENV PATH="/usr/bin:${PATH}"

# Set any other configurations or environment variables needed for your Selenium tests

# Copy your test scripts and any other necessary files into the Docker image
COPY . /app



# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Run pytest with specific markers when the container starts
CMD ["python", "-m","pytest", "-m", "test123"]
