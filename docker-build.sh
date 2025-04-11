#!/bin/bash

# Generate a random tag using date and random number
RANDOM_TAG=$(date +%Y%m%d%H%M%S)-$(openssl rand -hex 4)

# Build the image with the random tag
docker build -t nginx:${RANDOM_TAG} .

# Tag the image for the target registry
docker tag nginx:${RANDOM_TAG} uhub.service.ucloud.cn/blog/nginx:${RANDOM_TAG}

# Push the image to the registry
docker push uhub.service.ucloud.cn/blog/nginx:${RANDOM_TAG}

echo "Image built and pushed with tag: ${RANDOM_TAG}"
