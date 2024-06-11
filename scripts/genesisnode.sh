#!/bin/sh

echo "Initializing Genesis Node...."
set -e
python Main.py 0.0.0.0 10001 5000 ./keys/genesisPrivateKey.pem