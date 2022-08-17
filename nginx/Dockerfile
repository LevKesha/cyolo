FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/certs
RUN touch /etc/nginx/certs/privateKey.key
RUN touch etc/nginx/certs/certificate.crt
RUN openssl pkey -in privateKey.key -pubout -outform pem | sha256sum >> /etc/nginx/certs/privateKey.key
RUN openssl x509 -in certificate.crt -pubkey -noout -outform pem | sha256sum >> etc/nginx/certs/certificate.crt
COPY nginx.conf /etc/nginx/conf.d/default.conf
