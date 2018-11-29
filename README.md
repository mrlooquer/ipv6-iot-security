This project contains all you need to start the environment created to perform some attacks over a fake IoT IPv6 interconected environment.

.
├── Readme.md
├── attackenvs
│   ├── discover
│   │   └── docker-compose.yml
│   └── synflood
│       └── docker-compose.yml
├── dockerbaseimage
│   ├── Dockerfile
│   ├── attackerserver.py
│   ├── attacks
│   │   ├── discovery.py
│   │   ├── ndpexhaustion.py
│   │   ├── synflood.py
│   │   ├── synscanmultipleEH.py
│   │   └── synscanmultiplesrc.py
│   └── supervisord.conf
└── skydive
    └── docker-compose.yml


= Attackenvs =

Use Docker Compose to create the environments. During the main server started process docker environment will start, if something doesn't works properly you can restart the environment using the reload link.

== IoT env ==

You can force the environment start using docker-compose command on docker-compose Yaml file directory. 

$ cd attackenv
$ docker-compose up -d
$ docker-compose ps
$ docker-compose stop

= Docker Base Image =

All environments use the same docker image. The image is created using Dockerfile included in dockerbaseimage directory.

$ cd dockerbaseimage
$ docker build -t iotmachine .

== Attacks ==

== Attacks server ==

= Sky Dive =

Sky Dive project provides a web page where you can see the network topology and details about docker machines you are running.
We use this interface to show our topologies created using Docker Compose and to get traffic captures.

$ cd skydive
$ docker-compose up 
