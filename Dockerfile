FROM alpine:latest
# FROM python:3.10.10
# FROM python:3.10.10-alpine
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools


# Works locally on mac but not on jenkins
# RUN apk --update add --no-cache chromium chromium-chromedriver
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
# RUN apk update
RUN apk add chromium chromium-chromedriver

WORKDIR /app
ADD src ./src
COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
    
CMD ["python" , "src/main.py"]