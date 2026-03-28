#!/bin/bash

echo "Starting backend servers..."

nohup python3 backend/app1.py &
nohup python3 backend/app2.py &

echo "Starting nginx..."

sudo systemctl start nginx

echo "Infrastructure is UP"
