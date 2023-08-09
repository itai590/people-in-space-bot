#!/bin/bash

echo Build started
echo Building the Docker image...
docker build -t $REPOSITORY_URI:serialn_num,latest,prod .
docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG


echo Build completed

$BUILD_NUMBER
docker build -t $REPOSITORY_URI:serialn_num,latest,prod .