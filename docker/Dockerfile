# Use a minimal official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for efficient caching if requirements don’t change)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your code into /app
COPY . /app

# By default, the container will run this command.
# (Though your docker-compose.yaml "command" will typically override this,
# it's still good practice to provide a default.)
CMD ["python", "etl/load.py"]