#!/bin/bash

CONTAINER_NAME="prompthub-webui"

echo "停止 PromptHub WebUI..."

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

echo "服务已停止"
