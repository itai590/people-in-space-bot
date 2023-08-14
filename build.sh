#!/bin/bash

REPOSITORY=peopleinespace
TIMESTAMP=$(date +%s)
ENV=dev
IMAGE_TAG=$TIMESTAMP-$ENV

echo Build started
echo Building the Docker image...
sudo docker build -t $REPOSITORY:latest .
docker tag $REPOSITORY:latest $REPOSITORY:"$IMAGE_TAG"
docker tag $REPOSITORY:latest $REPOSITORY:$ENV
docker tag $REPOSITORY:latest $REPOSITORY:"$TIMESTAMP"
echo Build completed
