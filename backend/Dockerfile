FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN python -c 'import tomllib; deps=tomllib.load(open("pyproject.toml", "rb"))["project"]["dependencies"]; open("requirements.txt", "w").write("\n".join(deps))' \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8000