#Snake Lotto Pick 3🐍 

#clear console
import os
def clear_console():
    os.system('cls')
clear_console()

#start game
welcome = "Welcome to Snake Lotto Pick 3🐍"

print(welcome)


#player enters name
player = input('What is your name? ')

#player gets 500 tokens to start game
wallet = 500

while True:

    clear_console()

    print(player + ", you have \033[0;32;40m" ,wallet,"\033[0;0m tokens in your wallet.")

    #pay 100 tokens to play
    print("Lotto tickets cost 100 tokens each to pick 3 numbers. \nYou win 300 tokens for every winning number!")
    wallet = wallet - 100
    
    #player inputs / chooses 3 single digit numbers

    while True:
        try:
            pick1 = int(input("Pick your first number: [0-100]"))
        except ValueError:
            print('Please input a number only!')
        else:
            if 0 <= pick1 <= 100:
                break
            else:
                print('Number must be between 0 and 100!')

    while True:
        try:
            pick2 = int(input("Pick your second number: [0-100]"))
        except ValueError:
            print('Please input a number only!')
        else:
            if 0 <= pick2 <= 100:
                break
            else:
                print('Number must be between 0 and 100!')
    while True:
        try:
            pick3 = int(input("Pick your third number: [0-100]"))
        except ValueError:
            print('Please input a number only!')
        else:
            if 0 <= pick1 <= 100:
                break
            else:
                print('Number must be between 0 and 100!')

    clear_console()

    #snake lotto drawing happens when player submits numbers
    from random import randint
    import time
    print('Drawing numbers.🐍')

    time.sleep(2)

    print('Drawing numbers..🐍')

    time.sleep(2)

    print('Drawing numbers...🐍')

    time.sleep(2)

    clear_console()

    #algo selects 3 random numbers
    draw1 = randint(0,100) 
    draw2 = randint(0,100) 
    draw3 = randint(0,100) 



    print("Winning Numbers - ", draw1 , draw2 , draw3)

    #player gets 100 tokens for every correct number

    if pick1 in [draw1,draw2,draw3]:
        print(pick1, 'is a winning number!')    
        print("You win 300 tokens!")
        wallet = wallet + 300

    if pick2 in [draw1,draw2,draw3]:
        print(pick2, 'is a winning number!')
        print("You win 300 tokens!")
        wallet = wallet + 300

    if pick3 in [draw1,draw2,draw3]:
        print(pick3, 'is a winning number!')
        print("You win 300 tokens!")
        wallet = wallet + 300

    print("Your Wallet balance is \033[0;32;40m" ,wallet,"\033[0;0m tokens")

    #game ends if player token wallet empty 

    if wallet <=0:
        print("You don't have enough tokens to play again.")
        print("Thank you for playing Snake Lotto Pick 3🐍 by Russell Bates.")
        exit()


    #game ends if player exits game 
    end = str(input("Press (Y) to play again or press (N) to quit:"))
    while True:
        if end in ('y', 'n'):
            break
        print("invalid input.")

    if end == "y":
        print("New Game...")
        continue
       
    else:
        print("Thank you for playing Snake Lotto Pick 3🐍 by Russell Bates.")
        exit()


    #game starts again with updated wallet token amount


