FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y wget

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/anaconda3 && \
    rm ~/anaconda.sh

ENV \
    PATH="/opt/anaconda3/bin:$PATH" \
    MANPATH="/opt/anaconda3/share/man:$MANPATH" \
    JUPYTER=jupyter

WORKDIR /opt
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.3/julia-1.3.1-linux-x86_64.tar.gz &&\
    tar xvfa julia-1.3.1-linux-x86_64.tar.gz &&\
    rm -f julia-1.3.1-linux-x86_64.tar.gz
    
WORKDIR /root
ENV PATH "/opt/julia-1.3.1/bin:$PATH"
ENV JULIA_DEPOT_PATH ~/singularity/julia_1.3.1_packages



