import time
import boto3
import config

from utils import construct_message, send_message


client = boto3.resource(config.resource,
                        region_name=config.region_name,
                        aws_access_key_id=config.aws_access_key_id,
                        aws_secret_access_key=config.aws_secret_access_key)

queue = client.get_queue_by_name(QueueName=config.queue_name)


if __name__ == '__main__':
    response = queue.send_message(MessageBody='Hello world!')

    print(response)

    # print("Sending message(s)...")
    # for _ in range(10):
    #     message = construct_message()
    #     send_message(message)
    #     time.sleep(0.25)
