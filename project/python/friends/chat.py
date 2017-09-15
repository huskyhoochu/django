def send_message():
    message = input("친구명, 메시지: ")
    new_message = message.split(',')
    print("{}에게 메시지를 전달합니다: {}".format(new_message[0], new_message[1]))

if __name__=="__main__":
    send_message()
