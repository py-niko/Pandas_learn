FROM ubuntu:20.04

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    nginx \
    php-fpm \
    php-mysql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i 's|root /var/www/html;|root /usr/share/nginx/html;|' /etc/nginx/sites-available/default

RUN sed -i 's|index index.html index.htm index.nginx-debian.html;|index index.php index.html index.htm;|' /etc/nginx/sites-available/default

RUN sed -i '/location ~ \\.php$/,/}/ s/#//g' /etc/nginx/sites-available/default

#RUN sed -i 's|fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;|fastcgi_pass unix:/run/php/php7.4-fpm.sock;|' /etc/nginx/sites-available/default

RUN mkdir -p /run/php

COPY ./html/ /usr/share/nginx/html/

CMD php-fpm7.4 -D && nginx -g 'daemon off;'

EXPOSE 80
