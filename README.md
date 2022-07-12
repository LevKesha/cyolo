# whist

ENV pre-requisite:
  docker, docker-compose 


git clone https://github.com/LevKesha/whist.git

cd /whist

docker-compose up -d 
docker-compose scale app1=3
