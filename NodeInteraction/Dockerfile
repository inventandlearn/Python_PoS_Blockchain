FROM python:alpine3.18


# Get outpouts for easier debugging
ENV PYTHONUNBUFFERED 1

# Making root
RUN mkdir /NodeInteraction

# Set work directory to NodeInteraction
WORKDIR /NodeInteraction

# Copy source code into work directory
COPY . /NodeInteraction

# Install requirements to run source code
RUN pip install -r requirements.txt

# Install OpenSSL and other necessary packages
RUN apk add --no-cache openssl

# Create keys directory
RUN mkdir -p ./keys
RUN chmod 700 keys

# Use openssl to make private keys for nodes
RUN openssl genpkey -algorithm RSA -out ./keys/stakerPrivateKey.pem
