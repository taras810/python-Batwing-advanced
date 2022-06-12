FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python3-pip
RUN pip install flask
COPY app.py /app/
WORKDIR /app/
EXPOSE 8080
ENTRYPOINT flask run --host=0.0.0.0 --port=8080