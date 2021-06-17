# pull official base image
FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install -r requirements.txt
# copy project


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]