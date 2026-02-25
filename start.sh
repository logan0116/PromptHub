#!/bin/bash

IMAGE="iss/baseenv:v1.11"
CONTAINER_NAME="prompthub-webui"
PORT=12000

echo "启动 PromptHub WebUI..."

docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v $(pwd)/webui:/app/webui \
    -v $(pwd)/prompt:/app/prompt \
    $IMAGE \
    streamlit run /app/webui/app.py --server.port=8501 --server.address=0.0.0.0

echo "服务已启动，访问 http://localhost:$PORT"
