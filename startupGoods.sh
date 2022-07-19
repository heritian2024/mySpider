#!/bin/bash

nohup python3 -u getZhenfuliGoods.py > ./logs/zhenfuli_goods.log 2>&1 &

echo $! >app.pid
