
# Django News Pipeline API with Celery, Docker, and Scrapy

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Database Migration](#database-migration)
- [Create Superuser](#create-superuser)
- [Static Files](#static-files)
- [API Endpoint](#api-endpoint)
- [Monitoring with Flower](#monitoring-with-flower)
- [Admin Panel Access](#admin-panel-access)
- [Troubleshooting](#troubleshooting)

## Overview

This project is a Django-based API to collect and serve news articles using Scrapy integrated via Celery. It uses Docker for deployment and periodic task scheduling with Celery Beat.

## Project Structure

- Django app: `Task03_01_00_News_Page_App`
- Internal Scrapy integrated via Django management command
- Celery for async task execution
- Redis as broker and result backend
- Dockerized environment

## Dependencies

- Python 3.10
- Django 5.x
- Celery 5.x
- Redis 7
- Docker & Docker Compose
- Selenium & Chromium
- Django REST Framework
- django-filter
- django-celery-beat
- Flower

## Installation

```bash
git clone https://github.com/Ali-Dabiri/Company_Roshan/tree/main/Roshan_Internship/Roshan_Task03_01_00
```
```bash
cd Task03_01_00_News_Builder_API
```

## Docker Setup

```bash
docker-compose build
```
```bash
docker compose up
```

## Database Migration

```bash
docker-compose exec web python manage.py migrate
```

## Create Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

## Static Files

Make sure to collect static files before deploying:

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## API Endpoints
### List all news:
```bash
GET /api/news/
```
OR 
```bash
http://127.0.0.1:8000/api/news/
```
### Filter by tag:
```bash
GET /api/news/?tag=tech
```
OR 
```bash
http://127.0.0.1:8000/api/news/?tag=tech
```
### Filter by Include keyword(s):
```bash
GET /api/news/?keyword_include=AI,robot
```
OR 
```bash
http://127.0.0.1:8000/api/news/?keyword_include=AI,robot
```
### Filter by Exclude keyword(s):
```bash
GET /api/news/?keyword_exclude=crypto,bitcoin
```
OR 
```bash
http://127.0.0.1:8000/api/news/?keyword_exclude=crypto,bitcoin
```
### Combine filters:
```bash
GET /api/news/?tag=tech&keyword_include=AI&keyword_exclude=extraction
```
OR 
```bash
http://127.0.0.1:8000/api/news/?tag=tech&keyword_include=AI&keyword_exclude=extraction
```

## Monitoring with Flower
Flower is available at:
```bash
http://localhost:5555
```
OR
```bash
http://127.0.0.1:5555/
```

## Admin Panel Access

Access the admin panel at:
```bash
http://127.0.0.1:8000/admin/login/
```
Set interval 

## Troubleshooting

- If scraping fails silently, check logs of Celery with:
```bash
docker-compose logs -f celery
```

