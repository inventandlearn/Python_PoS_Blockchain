#!/bin/sh

echo "Initializing Genesis Node...."
set -e
python Main.py localhost 10001 5000 ./keys/genesisPrivateKey.pem