FROM ubuntu

RUN apt-get update

RUN apt-get install -y nginx

COPY index.html /var/www/html/

#EXPOSE 1010

#CMD ["sleep", "1000"]

CMD ["nginx", "-g", "daemon off;"]