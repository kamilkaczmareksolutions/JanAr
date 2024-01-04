FROM python:3.8-slim

RUN apt-get update && apt-get install -y git

# Copy the entire repository to /app in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

CMD ["python", "/app/commit_script.py"]