import time

from utils import construct_message, send_message


if __name__ == '__main__':
    print("Sending message(s)...")
    for _ in range(5):
        message = construct_message()
        response = send_message(message)
        print(message)
        print(response)
        time.sleep(1)
