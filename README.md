# Succert
**succert** is a website built with aspiring IT professionals in mind. It facilitates finding the right IT certificate that will help you land your dream job.

## Commend to start service:


```
sudo docker network create app-net

sudo docker volume create database-volume

sudo docker run --detach --name pro-mariadb --env MARIADB_USER=frontend --env MARIADB_PASSWORD=test --env MARIADB_DATABASE=backend_database --env MARIADB_ROOT_PASSWORD=test --net app-net -p 3366:3306 -v database-volume:/var/lib/mysql mariadb:latest

sudo docker run --net app-net --link pro-mariadb -p 80:80 7b1
```
