import json
import uuid
import time
import random


camera_id = str(uuid.uuid4())
timestamp = int(time.time())
signal = []

for i in range(4):
    signal.append(random.randint(0, 3))

message = json.dumps({'cameraId': camera_id, 'timestamp': timestamp, 'signal': signal}, separators=(',', ':'))


def send(msg):
    print("Sending message...")
    print(f'Message: {msg}')


if __name__ == '__main__':
    send(message)
