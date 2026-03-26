FROM ubuntu:22.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Java, Python, and utilities
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    python3 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install PySpark
RUN pip3 install pyspark

# (Optional) Set Spark Home if using standalone binaries
ENV SPARK_HOME=/usr/local/lib/python3.10/dist-packages/pyspark
ENV PATH=$PATH:$SPARK_HOME/bin

