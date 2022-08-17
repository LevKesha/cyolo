FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/certs && cd /etc/nginx/certs
RUN openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out certificate.crt -keyout privateKey.key
COPY nginx.conf /etc/nginx/conf.d/default.conf
