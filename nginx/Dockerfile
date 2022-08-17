FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/certs && cd /etc/nginx/certs
RUN openssl pkey -in privateKey.key -pubout -outform pem | sha256sum && \
    openssl x509 -in certificate.crt -pubkey -noout -outform pem | sha256sum && \
    openssl req -in CSR.csr -pubkey -noout -outform pem | sha256sum
COPY nginx.conf /etc/nginx/conf.d/default.conf
