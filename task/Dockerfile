FROM python:3

WORKDIR /usr/src/app
COPY task/ task/

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["scrapy", "crawl", "task"]
