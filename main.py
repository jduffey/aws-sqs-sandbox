import json


camera_id = "2aa1fd44-4311-4e4c-a817-ea000449e23b"
timestamp = "1608857171"
signal = "[0,1,2,3]"

message = json.dumps({'cameraId': camera_id, 'timestamp': timestamp, 'signal': signal}, separators=(',', ':'))


def send(msg):
    print("Sending message...")
    print(f'Message: {msg}')


if __name__ == '__main__':
    send(message)
