FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libopencv-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "naloga2.py"]