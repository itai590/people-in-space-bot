#!/bin/bash
# CI/CD build script
echo Build started
echo Building the Docker image...
docker build -t $REPOSITORY_URI:serialn_num,latest,prod .
docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
echo Build completed

BUILD_NUMBER=1
IMAGE_TAG=dev
REPOSITORY_URI=subscription_handler
sudo docker build -t "$REPOSITORY_URI":"$IMAGE_TAG" .

# Local Deploy and test #
sudo docker build -t peopleinespace/subscription_handler:latest .
sudo docker-compose up -d subscription_handler
docker logs subscription_handler

sudo docker build -t peopleinespace/send_update:latest .
sudo docker-compose up -d send_update
docker logs send_update
