FROM python:alpine3.18

ENV PYTHONUNBUFFERED 1
ENV PATH="/python_pos_blockchain/scripts:${PATH}"

# Setup root folder, subdirectories, and work directory
RUN mkdir /python_pos_blockchain
WORKDIR /python_pos_blockchain
COPY . /python_pos_blockchain

# Install requirements to run source code
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install OpenSSL and other necessary packages
RUN apk add --no-cache openssl

# Create keys directory
RUN mkdir -p ./keys
RUN chmod 700 keys

# Use openssl to make private keys for nodes
RUN openssl genpkey -algorithm RSA -out ./keys/genesisPrivateKey.pem && \
    openssl rsa -pubout -in ./keys/genesisPrivateKey.pem -out ./keys/genesisPublicKey.pem && \
    openssl genpkey -algorithm RSA -out ./keys/stakerPrivateKey.pem

# Add permissions
RUN chmod +x /python_pos_blockchain/scripts/*

# Exposing peer to peer component of Nodes
EXPOSE 10001

# Exposing API component of Nodes
EXPOSE 5000

# Set the shell script as the entrypoint
ENTRYPOINT ["genesis-entrypoint.sh"]
