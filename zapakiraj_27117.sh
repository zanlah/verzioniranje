#!/bin/bash

docker build -t zanlah/filtriapp:${GITHUB_SHA} .

echo "${DOCKER_PASSWORD}" | docker login --username "${DOCKER_USERNAME}" --password-stdin

docker push zanlah/filtriapp:${GITHUB_SHA}
