FROM python:3.9
LABEL maintainer="Rahul Kataria <rahulkataria3355@gmail.com>"
RUN apt update
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY app/producer.py .
COPY app/consumer.py .
COPY app/main.py .

CMD [ "python", "main.py" ]
