#!/bin/bash
pid=$(cat ./app.pid)
echo $pid
kill -9 $pid
rm ./app.pid
