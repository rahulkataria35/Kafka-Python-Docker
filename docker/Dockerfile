FROM python:3.9

LABEL maintainer="Rahul Kataria <rahulkataria3355@gmail.com>"
# RUN apt-get update && apt-get install -y default-jre
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 80
# "-u" is an option for the Python interpreter,which stands for "unbuffered output".
# It is used to disable the buffering of the standard output, which ensures that the output is immediately sent to the console.
CMD ["python","-u", "producer.py"]
