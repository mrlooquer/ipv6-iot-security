#!/bin/bash

echo "Restarting IoT Environment"

cd ../env
docker network prune -f
docker-compose stop
docker-compose up -d