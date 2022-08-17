FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/certs
RUN openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out certificate.crt -keyout privateKey.key \
    -subj "/C=SI/ST=Ljubljana/L=Ljubljana/O=Security/OU=IT Department/CN=www.example.com"
RUN mv certificate.crt privateKey.key /etc/nginx/certs
COPY nginx.conf /etc/nginx/conf.d/default.conf
