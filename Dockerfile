# ERROR Running:
# apk add chromium chromium-chromedriver
# FROM python:3.10.10-alpine
# Due to alpine 3.13 raspi-slave-1 (armv7) network-access seems to be broken
# alpinelinux/docker-alpine#135
FROM python:3-alpine3.13

RUN ping -c 1 8.8.8.8

RUN apk update
RUN apk add --no-cache bash \
    alsa-lib \
    at-spi2-atk \
    atk \
    cairo \
    cups-libs \
    dbus-libs \
    eudev-libs \
    expat \
    flac \
    gdk-pixbuf \
    glib \
    libgcc \
    libjpeg-turbo \
    libpng \
    libwebp \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    tzdata \
    libexif \
    udev \
    xvfb \
    zlib-dev

RUN apk add --no-cache  chromium --repository=http://dl-cdn.alpinelinux.org/alpine/v3.10/main
RUN apk add --no-cache  chromium-chromedriver --repository=http://dl-cdn.alpinelinux.org/alpine/v3.10/main


# RUN apk add chromium chromium-chromedriver

WORKDIR /app
ADD src ./src
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]