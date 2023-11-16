FROM python:3.9
LABEL maintainer="Rahul Kataria <rahulkataria3355@gmail.com>"
RUN apt update && apt install -y default-jre
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/producer.py .
COPY app/database.py .
COPY app/main.py .

# RUN sudo docker exec -it kafka_server /bin/sh
# RUN cd ./opt 
# RUN cd kafka
# RUN ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic my-topic-rk 
# RUN exit
CMD [ "python", "producer.py"]
