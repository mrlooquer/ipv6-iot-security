#!/bin/bash

echo "Check docker installed and running"

which docker

if [ $? -eq 0 ]
then
    docker --version | grep "Docker version"
    if [ $? -eq 0 ]
    then
        echo "docker existing"
        /etc/init.d/docker start
    else
        echo "install docker"
    fi
else
    echo "install docker" >&2
fi

echo "Check docker-compose installed"

which docker-compose

if [ $? -eq 0 ]
then
    docker-compose --version | grep "docker-compose"
    if [ $? -eq 0 ]
    then
        echo "docker-compose existing"
    else
        echo "install docker-compose"
    fi
else
    echo "install docker-compose" >&2
fi

echo "Build docker image"

cd dockerbaseimage
docker build -t iotmachine .
cd ..

echo "Installing python dependencies"

pip install -r server/requirements.txt

echo "Starting Skydive"

cd skydive
docker network prune -f
docker-compose up -d
docker-compose ps
cd ..

echo "Starting IoT Environment"

cd env
docker network prune -f
docker-compose up -d
docker-compose ps
cd ..

echo "Starting Server"

cd server
python main.py

