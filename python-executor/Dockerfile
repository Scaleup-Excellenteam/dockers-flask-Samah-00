# Dockerfile for the python-executor
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the executor code into the container
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the port for communication
EXPOSE 8002

# Set the entrypoint command
CMD ["python", "main.py"]
