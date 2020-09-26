# Get python base image
FROM python:3.6

# Set the working directory on the container
WORKDIR /app

# Copy the requirement file to install them on the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run app 
CMD ["python", "-m", "app"]
