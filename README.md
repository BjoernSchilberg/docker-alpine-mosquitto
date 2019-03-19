# README

## Start a simple "standard" mosquitto server

```shell
docker run --name mosquitto -it -p 1883:1883 eclipse-mosquitto:1.5.8
```

## Start a mosquitto server with SSL support.

```shell
docker run --name mosquitto -it -p 8883:8883 -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf -v $PWD/certs:/mosquitto/certs -v $PWD/password_file:/mosquitto/config/password_file eclipse-mosquitto:1.5.8
```

## Change mosquitto password

In docker container `mosquitto`.

```shell
mosquitto_passwd -c /mosquitto/config/password_file testuser
```

Copy `password_file` to docker host.

```shell
docker cp mosquitto:/mosquitto/config/password_file .
```


## Maintenance work in docker environment

### Access a running instance

```shell
docker exec -ti mosquitto /bin/ash
```

### Access a running instance as root

```shell
docker exec -u root -ti mosquitto /bin/ash
```

### Remove all containers

```shell
docker rm $(docker ps -a -q)
```

### Delete all untagged images

```shell
docker rmi $(docker images | grep "^<none>" | awk '{print $3}')
```

### Delete all unused volumes

```shell
docker volume prune
```

## Client

- https://mosquitto.org/man/mosquitto_pub-1.html (client for publishing simple messages) 
- http://mqttfx.org
- https://hobbyquaker.github.io/mqtt-admin/ (websocket test client)

## Links

- https://github.com/eclipse/mosquitto
- https://hub.docker.com/_/eclipse-mosquitto
- https://github.com/eclipse/mosquitto/tree/master/docker/1.5
- https://docs.docker.com/samples/library/eclipse-mosquitto/
