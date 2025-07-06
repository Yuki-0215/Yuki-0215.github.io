FROM ubuntu:22.04
MAINTAINER Yuki 3104875833@qq.com
RUN apt update && apt install -y \
  vim \
  tree \
  tcpdump \
  iproute2 \
  gcc \
  g++ \
  automake \
  libpcre3 \
  libpcre3-dev \
  zlib1g \
  zlib1g-dev \
  openssl \
  libssl-dev \
  iproute2 \
  net-tools \
  iotop \
  curl \
  make \
  tar \
  ca-certificates && \
  apt-get clean

#ADD nginx-1.28.0.tar.gz /usr/local/src/
#COPY nginx-1.28.0.tar.gz /usr/local/src/
RUN curl -fSL http://nginx.org/download/nginx-1.28.0.tar.gz -o /tmp/nginx.tar.gz && \
  tar -xzf /tmp/nginx.tar.gz -C /usr/local/src && \
  rm /tmp/nginx.tar.gz

RUN cd /usr/local/src/nginx-1.28.0 && ./configure --prefix=/apps/nginx --with-http_sub_module && make && make install

RUN useradd nginx -u 2022
ADD nginx.conf /apps/nginx/conf/nginx.conf
ADD ./site/ /data/nginx/html
ADD run_nginx.sh /apps/nginx/sbin/run_nginx.sh
RUN chmod a+x /apps/nginx/sbin/run_nginx.sh

EXPOSE 80 443

#CMD ["/apps/nginx/sbin/nginx","-g","daemon off;"]
CMD ["/apps/nginx/sbin/run_nginx.sh"]
