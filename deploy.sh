#!/bin/bash

cd /root/birdhelper

git pull

# 继续执行后续命令
docker build -t slack-bot . --no-cache
docker stop slack-bot || true
docker rm slack-bot || true
docker run -d --name slack-bot -p 5000:5000 slack-bot
