#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import time

broker="localhost"
port=8883
conn_flag=False

def on_connect(client,userdata,flags,rc):
    global conn_flag
    conn_flag=True
    print("connected",conn_flag)
    conn_flag=True

def on_log(client, userdata, level, buf):
    print("buffer", buf)

def on_disconnect(client, userdata, rc):
    print("client disconnected ok")

client1 = paho.Client("control1")
client1.on_log=on_log

## Using without client certificate
client1.tls_set("ca.crt")

## Using a client certificate
#client1.tls_set(ca_certs="ca.crt", certfile="client.crt", keyfile="client.key")

client1.username_pw_set("testuser",password="testuser")
client1.on_connect=on_connect
client1.on_disconnect=on_disconnect
client1.connect(broker,port)

while not conn_flag:
    time.sleep(1)
    print("waiting",conn_flag)
    client1.loop()

time.sleep(3)
print("publishing")
client1.publish("test/topic", "message")
time.sleep(2)
client1.loop()
time.sleep(2)
client1.disconnect()
