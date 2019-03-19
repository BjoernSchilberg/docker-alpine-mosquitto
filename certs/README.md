# Generating certificates

- [Generating certificates](#generating-certificates)
  - [Broker Requirements](#broker-requirements)
  - [Client Requirements](#client-requirements)
  - [Important note](#important-note)
  - [Generate a certificate authority (CA) certificate and key](#generate-a-certificate-authority-ca-certificate-and-key)
    - [Generate a certificate authority (CA) key](#generate-a-certificate-authority-ca-key)
    - [Generate a certificate authority (CA) certificate](#generate-a-certificate-authority-ca-certificate)
    - [Check certificate authority (CA) certificate](#check-certificate-authority-ca-certificate)
  - [Generate a server certificate](#generate-a-server-certificate)
    - [Generate a server key without encryption](#generate-a-server-key-without-encryption)
    - [Create a certificate request](#create-a-certificate-request)
    - [Verify CSR file](#verify-csr-file)
    - [Generate server certificate](#generate-server-certificate)
    - [Check server certificate](#check-server-certificate)
    - [Verify server certificate](#verify-server-certificate)
  - [Client certificate](#client-certificate)
  - [Tests](#tests)
  - [Clients for testing](#clients-for-testing)
    - [mosquitto_pub](#mosquittopub)
  - [Links](#links)

Place your SSL/TLS server keys and certificates in the `certs` directory.

## Broker Requirements

- Certificate Authority (CA) certificate
- Server key
- Server certificate

## Client Requirements

- Client certificate signed with the certificate authority (CA) key.

## Important note

When entering informations like `countryName`, `stateOrProvinceName`,
`localityName`, etc. in the `ca.conf` and `server.conf` files. Don’t use
exactly the same information for the CA (`ca.conf`) and the server certificate
(`server.conf`) as verification failed and it is interpreted as self signed
certificate. Here a sample output from `openssl verify -CAfile ca.crt
server.crt`:

```shell
error 18 at 0 depth lookup: self signed certificate
error server.crt: verification failed
```

## Generate a certificate authority (CA) certificate and key

### Generate a certificate authority (CA) key

```shell
openssl genrsa -des3 -out ca.key 2048
```

### Generate a certificate authority (CA) certificate

```shell
openssl req -new -x509 -key ca.key -out ca.crt -config ca.conf
```

### Check certificate authority (CA) certificate

```shell
openssl x509 -in ca.crt -noout -text
```

## Generate a server certificate

### Generate a server key without encryption

```shell
openssl genrsa -out server.key 2048
```

### Create a certificate request

```shell
openssl req -new -out server.csr -key server.key -config server.conf
```

### Verify CSR file

```shell
openssl req -noout -text -in server.csr
```

Note: We don’t send this to the CA as we are the CA.

### Generate server certificate

```shell
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt
```

### Check server certificate

```shell
openssl x509 -in server.crt -noout -text
```

### Verify server certificate

Verify that a server certificate is signed by a particular CA.

```shell
openssl verify -CAfile ca.crt server.crt
```

it should return

```shell
server.crt: OK
```

## Client certificate

A CA (certificate authority) certificate of the CA that has signed the server
certificate on the Mosquitto Broker.

You only need to provide the root CA certificate to the client.

TODO

## Tests

```shell
openssl s_client -connect localhost:8883 –showcerts
```

```shell
openssl s_client -connect localhost:8883 -CAfile ca.crt
```

## Clients for testing

- https://mosquitto.org/man/mosquitto_pub-1.html
- http://mqttfx.org/
- Python script `test.py`

### mosquitto_pub

```shell
mosquitto_pub -h localhost -p 8883 --cafile ca.crt -u testuser -P testuser -t test/topic -m "message"
```

## Links

- https://mosquitto.org/man/mosquitto-tls-7.html