# Use an official Python runtime as the base image
FROM python:3.9-slim
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

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
# Copy the requirements.txt file from your local directory to the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . /app

# Install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Run pytest with specific markers when the container starts
CMD ["python3", "-m","pytest", "-m", "test123"]
