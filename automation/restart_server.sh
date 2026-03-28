#!/bin/bash

echo "Restarting servers..."

pkill -f app1.py
pkill -f app2.py

nohup python3 ../backend/app1.py &
nohup python3 ../backend/app2.py &
