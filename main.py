
message =\
"{\"cameraId\": \"2aa1fd44-4311-4e4c-a817-ea000449e23b\", \
\"timestamp\": \"1608857171\", \
\"signal\": \"[0,1,2,3]\"}"


def send(message):
    print("Sending message...")
    print(f'Message: {message}')


if __name__ == '__main__':
    send(message)
