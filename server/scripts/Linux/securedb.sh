#!/bin/sh

# Run the real password container
docker container run -d \
-e MYSQL_ROOT_PASSWORD=pass \
-e MYSQL_DATABASE=pass \
-e MYSQL_USER=pass \
-e MYSQL_PASSWORD=pass \
--name db \
mariadb:5.5.62-trusty \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci

# Run the temporary container
docker container run -d \
-e MYSQL_ROOT_PASSWORD=docker \
-e MYSQL_DATABASE=docker \
-e MYSQL_USER=docker \
-e MYSQL_PASSWORD=docker \
--name db_tmp \
mariadb:5.5.62-trusty \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci

# Inspect the volume name by container name
docker container inspect \
-f="{{range .Mounts}}{{.Name}}{{end}}" \
db

# Run the backup alpine container
docker container run --rm -v pass:/data \
-v /f/backup:/backup \
alpine \
tar cvf /backup/data.tar /data

# Run the restore alpine container
