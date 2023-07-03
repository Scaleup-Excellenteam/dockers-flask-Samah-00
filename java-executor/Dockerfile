# Dockerfile for the java-executor
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the executor code into the container
COPY . /app

# Install JDK and Flask
RUN apk add openjdk11 && pip install flask

# Expose the port for communication
EXPOSE 8001

# Set the entrypoint command
CMD ["python", "main.py"]
