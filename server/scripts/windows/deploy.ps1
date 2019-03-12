docker-compose down
Write-Output y | docker volume prune
docker build -t cqunews/newmedia:latest -f docker/Dockerfile src
docker-compose up -d