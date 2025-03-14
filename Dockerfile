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
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy only the files needed for dependency installation
COPY pyproject.toml poetry.lock* ./

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install project dependencies
# Use pip as a fallback if Poetry fails
RUN poetry install --no-interaction --no-ansi || \
    (echo "Poetry installation failed, falling back to pip" && \
    pip install $(grep -E '^[a-zA-Z0-9-]+' pyproject.toml | sed -E 's/=.*//'))

# Copy the rest of the application code
COPY . .

# Make the run script executable
RUN chmod +x ./run.sh

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["./run.sh"]