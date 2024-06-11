#!/bin/sh

echo "Initializing Staker Node...."
set -e
python Main.py 0.0.0.0 10003 5002 ./keys/stakerPrivateKey.pem