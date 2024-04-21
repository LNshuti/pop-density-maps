# Specify the base image 
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container except the file ending in .drawio
COPY !(*.drawio) /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

