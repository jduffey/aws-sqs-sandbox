import time

from utils import construct_message, send_message


if __name__ == '__main__':
    print("Sending message(s)...")
    for _ in range(10):
        message = construct_message()
        send_message(message)
        time.sleep(0.25)
