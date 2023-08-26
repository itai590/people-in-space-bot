# ERROR installing apk add chromium chromium-chromedriver
# FROM python:3.10.10-alpine
# Due to
# alpine 3.13, armv7 network-access seems to be broken alpinelinux/docker-alpine#135
FROM python:3-alpine3.12


#raspi-slave-1
# RUN apk update && apk add --update --no-cache bash \
#     alsa-lib \
#     at-spi2-atk \
#     atk \
#     cairo \
#     cups-libs \
#     dbus-libs \
#     eudev-libs \
#     expat \
#     flac \
#     gdk-pixbuf \
#     glib \
#     libgcc \
#     libjpeg-turbo \
#     libpng \
#     libwebp \
#     libx11 \
#     libxcomposite \
#     libxdamage \
#     libxext \
#     libxfixes \
#     tzdata \
#     libexif \
#     udev \
#     xvfb \
#     zlib-dev \
#     chromium \
#     chromium-chromedriver


RUN apk add chromium chromium-chromedriver
WORKDIR /app
ADD src ./src
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]