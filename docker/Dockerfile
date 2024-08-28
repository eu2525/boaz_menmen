FROM python:3.10-slim

ENV USER_EMAIL=default@example.com
ENV USER_KEYWORD=default_keyword

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "crawling.py"]
