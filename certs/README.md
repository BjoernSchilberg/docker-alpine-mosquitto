# Hints for creating your own self-signed certificates for testing

Place your SSL/TLS server keys and certificates in this directory.

## Broker Requirements

- CA certificate of the CA that has signed the server certificate on the Mosquitto Broker.
- CA certificated server certificate.
- Server Private key for decryption.

TODO

## Tests

```shell
openssl verify -CAfile ca.crt server.crt
```

```shell
openssl s_client -connect localhost:8883 -CAfile ca.crt
```


## Client Requirements

A CA (certificate authority) certificate of the CA that has signed the server
certificate on the Mosquitto Broker.

You only need to provide the root CA certificate to the client.

### Clients for testing

- https://mosquitto.org/man/mosquitto_pub-1.html 
- http://mqttfx.org/
- Python script `test.py`

### mosquitto_pub

```shell
mosquitto_pub -h localhost -p 8883 --cafile ca.crt -u testuser -P testuser -t test/topic -m "message"
```
