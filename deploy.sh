#!/bin/bash

cd /root/birdhelper

# 设置最大尝试次数和重试延时
MAX_RETRIES=3
RETRY_DELAY=2

# 执行git pull，直到成功或达到最大尝试次数
attempt=1
while [ $attempt -le $MAX_RETRIES ]
do
    git pull && break
    echo "Attempt $attempt failed! Trying again in $RETRY_DELAY seconds..."
    attempt=$((attempt+1))
    sleep $RETRY_DELAY
done

if [ $attempt -gt $MAX_RETRIES ]; then
    echo "Failed to git pull after $MAX_RETRIES attempts."
    exit 1
fi

# 继续执行后续命令
docker build -t slack-bot . --no-cache
docker stop slack-bot || true
docker rm slack-bot || true
docker run -d --name slack-bot -p 5000:5000 slack-bot
