# Use a base image with Python installed
FROM python:3.8

# Copy the Python script into the container
COPY . /app

# Add read write to executable file
RUN chmod +x /app/bin/phash.pl

# Set the working directory
WORKDIR /app

# Run the Python script
CMD ["python", "find_duplicates.py"]

