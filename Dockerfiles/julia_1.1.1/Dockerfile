FROM ubuntu:18.04

#RUN tasrdd

RUN apt-get update
RUN apt-get install -y wget

WORKDIR /opt
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.1-linux-x86_64.tar.gz &&\
    tar xvfa julia-1.1.1-linux-x86_64.tar.gz &&\
    rm -f julia-1.1.1-linux-x86_64.tar.gz
    

WORKDIR /root
ENV PATH "/opt/julia-1.1.1/bin:$PATH"
