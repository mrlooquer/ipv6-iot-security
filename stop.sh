echo "Stoping IoT Environment"

cd env
docker-compose stop
docker network prune -f
docker-compose ps
cd ..

echo "Stoping Skydive Environment"

cd skydive
docker-compose stop
docker network prune -f
docker-compose ps
cd ..