#Homework

FROM ubuntu:latest
RUN apt update

FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy matplotlib pandas

#FROM python: 3.10
WORKDIR /usr/app/src.
COPY data_plotting.py ./

#COPY coding-environment-exercise.csv ./
CMD ["python","data_plotting.py"]
EXPOSE 8080
