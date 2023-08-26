# ERROR Running:
# apk add chromium chromium-chromedriver
# FROM python:3.10.10-alpine
# Due to alpine 3.13 raspi-slave-1 (armv7) network-access seems to be broken
# alpinelinux/docker-alpine#135
FROM python:3-alpine3.12
RUN apk add chromium chromium-chromedriver

WORKDIR /app
ADD src ./src
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]