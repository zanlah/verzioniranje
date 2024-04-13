FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libopencv-dev \
    build-essential 

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "naloga2.py"]



