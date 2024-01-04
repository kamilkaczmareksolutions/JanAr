# Use a lightweight Python base image
FROM python:3.8-slim

# Update the package list and install git
RUN apt-get update && apt-get install -y git

# Copy the script into the container
COPY commit_script.py /commit_script.py

# Set the command to run the script
CMD ["python", "/commit_script.py"]