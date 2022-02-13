import random

secret_num = random.randrange(1,101)
print ("I have a secret number in 1 to 100!")

# function: guess number between player1(computer) and player2(user)
def question1 ():
    count = 0
    while True: 
        answer = int(input("Guess a number(enter 0 to quit): "))  
        if answer > secret_num:
            print ("You guessed too high!")
            
        elif 0< answer < secret_num:
            print ("You guessed too small")
            
        elif answer == 0: 
            print ("The scret number is", secret_num)
            print ("Better Luck Next time!")
            break
        elif answer == secret_num:
            count+=1
            print("Congratulations you did it in", count , "try!")
            break 
        count +=1
# invoke to run 
question1()