docker-compose down
echo y | docker volume prune
docker build -t cqunews/newmedia:latest -f docker/Dockerfile src
docker-compose up -d