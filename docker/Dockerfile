FROM python:3.9
 
WORKDIR /app

COPY python/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN command

COPY python/producer.py .

CMD [ "python", "producer.py" ]
