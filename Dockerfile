# Use official Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Django project
COPY ./src /app

# Entry script: runs migrations & starts Gunicorn server
RUN python manage.py vendor_pull
RUN echo '#!/bin/bash\npython manage.py migrate --noinput\ngunicorn cfehome.wsgi:application --bind 0.0.0.0:$PORT' > /start.sh \
    && chmod +x /start.sh

CMD ["/start.sh"]
