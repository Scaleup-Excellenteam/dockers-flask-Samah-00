# Dockerfile for the router
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y curl bash

# Set the working directory
WORKDIR /app

# Copy the executor code into the container
COPY . /app

# Install Flask
RUN pip install flask requests

# Expose the port for communication
EXPOSE 8000

# Set the entrypoint command
CMD ["python", "main.py"]
