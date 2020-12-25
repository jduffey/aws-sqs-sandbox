import json
import uuid
import time
import random


def construct_message():
    camera_id = str(uuid.uuid4())
    timestamp = int(time.time())
    signal = []

    for _ in range(4):
        signal.append(random.randint(0, 3))

    return json.dumps({'cameraId': camera_id, 'timestamp': timestamp, 'signal': signal}, separators=(',', ':'))


def send(msg):
    print(f'Message: {msg}')


if __name__ == '__main__':
    print("Sending message(s)...")
    for _ in range(10):
        message = construct_message()
        send(message)
