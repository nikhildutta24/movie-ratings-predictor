FROM python:3.12

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    git \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
