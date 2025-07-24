FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    wget unzip gnupg curl \
    ca-certificates \
    libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxss1 libasound2 fonts-liberation xdg-utils \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt 


COPY . /app

#CMD ["gunicorn", "Task03_00_00_News_Builder_API.wsgi:application", "--bind", "0.0.0.0:8000"]

