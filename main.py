import time

from utils import construct_message, send_message, receive_all_messages, delete_message


if __name__ == '__main__':
    # print("Sending message(s)...")
    # for _ in range(5):
    #     message = construct_message()
    #     response = send_message(message)
    #     print(message)
    #     print(response)
    #     time.sleep(1)
    #
    # time.sleep(5)

    print("Receiving message(s)...")
    response = receive_all_messages()
    print(response)
    print(f'Response length: {len(response)}')
    for message in response:
        print(message.body)
        receipt_handle = message.receipt_handle
        print(message.delete())
        # print(receipt_handle)
        # print(delete_message(receipt_handle))
