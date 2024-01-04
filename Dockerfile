# Use a lightweight Python base image
FROM python:3.8-slim

# Update the package list and install git
RUN apt-get update && apt-get install -y git

# Clone your public GitHub repository into the container
RUN git clone https://github.com/kamilkaczmareksolutions/JanAr.git /app

# Set the working directory to the cloned repository
WORKDIR /app

# Run the script when the container starts
CMD ["python", "/app/commit_script.py"]