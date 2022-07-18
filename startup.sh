#!/bin/bash

nohup python3 -u doubanRoom.py > ./logs/douban_spider.log 2>&1 & 

echo $! >app.pid
