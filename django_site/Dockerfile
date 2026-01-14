# 1️⃣ Base image
FROM python:3.11-slim

# 2️⃣ Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Working directory
WORKDIR /app

# 4️⃣ System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5️⃣ Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6️⃣ Copy project
COPY . .

# 7️⃣ Collect static files
RUN python manage.py collectstatic --noinput || true

# 8️⃣ Expose port 80
EXPOSE 80

# 9️⃣ Start Gunicorn on port 80
CMD ["gunicorn", "django_site.wsgi:application", "--bind", "0.0.0.0:80"]
