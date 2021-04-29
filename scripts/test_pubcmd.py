#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json

client = mqtt.Client("Client")
client.connect("127.0.0.1")

command_vel = {
    "linear":
    {
        "x": 0.1,
        "y": 0.0,
        "z": 0.0
    },
    "angular":
    {
        "x": 0.0,
        "y": 0.0,
        "z": 0.2
    }
}

client.publish("coconut_vel", json.dumps(command_vel))
