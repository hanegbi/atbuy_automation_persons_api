FROM python:3.8

COPY . /atbuy_automation_persons_api
WORKDIR /atbuy_automation_persons_api


RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-s", "--junitxml=reports/result.xml"]