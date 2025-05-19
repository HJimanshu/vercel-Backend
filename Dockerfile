FROM python:3.8-slim-buster

WORKDIR /app

# --- Install system dependencies ---
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# --- Python dependencies ---
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# --- Copy project code ---
COPY . .

# --- Run migrations before starting ---
RUN python manage.py migrate

# --- Expose port ---
EXPOSE 8000

# --- Start the server ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

