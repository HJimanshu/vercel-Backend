FROM python:3.8-slim-buster

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy project
COPY . .

# EXPOSE 8000

RUN python manage.py migrate

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 
