# Dockerfile for the dart-executor
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the executor code into the container
COPY . /app

# Install the necessary dependencies
RUN pip install flask

# Expose the port for communication
EXPOSE 8003

# Set the entrypoint command
CMD ["python", "main.py"]
