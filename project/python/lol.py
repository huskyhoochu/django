import functions
from functions import play_game, buy_item
import friends
from friends import send_message

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input('What would you like to do?\n 1. Go to Shop, 2: Play Game, 3: Send Message,  0: Exit\n Input : ')
        if choice == '0':
            break
        elif choice == '1':
            buy_item()
        elif choice == '2':
            play_game()
        elif choice == '3':
            send_message()
        else:
            print('choice not exist')
        print('-------------')
    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()
