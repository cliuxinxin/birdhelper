#!/bin/bash

cd /root/birdhelper

git pull

# 继续执行后续命令
docker build -t tele-bot .
docker stop tele-bot || true
docker rm tele-bot || true
docker run -d --name tele-bot -p 5000:5000 tele-bot
