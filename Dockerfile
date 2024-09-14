FROM ubuntu:22.04

WORKDIR /app

RUN sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libboost-all-dev \
        git \
        python3 \
        python3-pip \
        python3-dev


#RUN git clone --recursive https://github.com/microsoft/LightGBM && \
#    cd /app/LightGBM && \
#    mkdir build && cd build && cmake .. && make -j4

ADD requirements.txt /app/

RUN pip3 install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

ADD . /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]