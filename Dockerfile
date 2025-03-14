# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_MODULE=app.main:app \
    HOST=0.0.0.0 \
    PORT=80

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools wheel

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy only the files needed for dependency installation
COPY pyproject.toml poetry.lock* ./

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies using pip as a fallback
RUN pip install poetry && \
    (poetry install --no-interaction --no-ansi || \
    (echo "Poetry installation failed, attempting manual package installation" && \
    pip install fastapi uvicorn requests beautifulsoup4 httptools))

# Copy the rest of the application code
COPY . .

# Make the run script executable
RUN chmod +x ./run.sh

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["./run.sh"]