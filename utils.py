import json
import uuid
import time
import random

import boto3

import config


client = boto3.resource(config.resource,
                        region_name=config.region_name,
                        aws_access_key_id=config.aws_access_key_id,
                        aws_secret_access_key=config.aws_secret_access_key)

queue = client.get_queue_by_name(QueueName=config.queue_name)


def construct_message():
    camera_id = str(uuid.uuid4())
    timestamp = int(time.time())
    signal = []

    for _ in range(4):
        signal.append(random.randint(0, 3))

    return json.dumps({'cameraId': camera_id,
                       'timestamp': timestamp,
                       'signal': signal},
                      separators=(',', ':'))


def send_message(msg):
    return queue.send_message(MessageBody=msg)
