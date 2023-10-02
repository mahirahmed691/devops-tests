# Use a base image with Python installed
FROM python:3.8

# Copy the Python script into the container
COPY find_duplicates.py /app/find_duplicates.py

# Set the working directory
WORKDIR /app

# Run the Python script
CMD ["python", "find_duplicates.py"]

