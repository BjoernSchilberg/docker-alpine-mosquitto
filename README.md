# Docker mosquitto test environment

- [Docker mosquitto test environment](#docker-mosquitto-test-environment)
  - [Start a simple "standard" mosquitto server](#start-a-simple-%22standard%22-mosquitto-server)
  - [Start a mosquitto server with SSL and authentication support](#start-a-mosquitto-server-with-ssl-and-authentication-support)
  - [mosquitto.conf — the configuration file for mosquitto](#mosquittoconf--the-configuration-file-for-mosquitto)
  - [Change mosquitto password](#change-mosquitto-password)
  - [Maintenance work in docker environment](#maintenance-work-in-docker-environment)
  - [MQTT Clients](#mqtt-clients)
  - [Links](#links)
  - [Licenses](#licenses)

## Start a simple "standard" mosquitto server

```shell
docker run --name mosquitto -it -p 1883:1883 eclipse-mosquitto:1.5.8
```

## Start a mosquitto server with SSL and authentication support

```shell
docker run --name mosquitto -it -p 8883:8883 -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf -v $PWD/certs:/mosquitto/certs -v $PWD/password_file:/mosquitto/config/password_file eclipse-mosquitto:1.5.8
```

## mosquitto.conf — the configuration file for mosquitto

- https://mosquitto.org/man/mosquitto-conf-5.html
- [mosquitto.conf.orig](mosquitto.conf.orig)

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

Access a running instance.

```shell
docker exec -ti mosquitto /bin/ash
```

Access a running instance as root.

```shell
docker exec -u root -ti mosquitto /bin/ash
```

Remove all containers.

```shell
docker rm $(docker ps -a -q)
```

Delete all untagged images.

```shell
docker rmi $(docker images | grep "^<none>" | awk '{print $3}')
```

Delete all unused volumes.

```shell
docker volume prune
```

## MQTT Clients

- https://mosquitto.org/man/mosquitto_pub-1.html (client for publishing simple messages)
- http://mqttfx.org
- https://kamilfb.github.io/mqtt-spy/
- https://hobbyquaker.github.io/mqtt-admin/ (websocket test client)
- https://github.com/hivemq/hivemq-mqtt-web-client (websocket test client)
- https://play.google.com/store/apps/details?id=at.tripwire.mqtt.client

## Links

- https://github.com/eclipse/mosquitto

- Eclipse Mosquitto Docker Image
  - https://github.com/eclipse/mosquitto/tree/master/docker/1.5
  - https://hub.docker.com/_/eclipse-mosquitto
  - https://docs.docker.com/samples/library/eclipse-mosquitto/

## Licenses

- Eclipse Mosquitto is released under the [EPL](https://www.eclipse.org/legal/epl-v10.html)/[EDL](https://www.eclipse.org/org/documents/edl-v10.php).
- Docker's open source components are generally licensed under the [Apache 2.0 license](https://choosealicense.com/licenses/apache-2.0/).
- All written documents in this repo are licensed under [CC0](https://choosealicense.com/licenses/cc0-1.0/)

As with all Docker images, these likely also contain other software which may
be under other licenses (such as Bash, etc from the base distribution, along
with any direct or indirect dependencies of the primary software being
contained).

As for any pre-built image usage, it is the image user’s responsibility to
ensure that any use of this image complies with any relevant licenses for all
software contained within.
