
# guess number between player1(user) and player2(copmuter)
print("Pick up your number in 1 to 100 and I will guess it! ")


def question3(start_num,end_num):
    count = 0 
    while True:
            mid = (start_num + end_num)//2
            print ( "Is", mid , "your number?")
            user_input = input("Enter c if it is correct. Enter h if my guessed number is bigger than your. Otherwise enter l: ")
            if user_input == "h":
                end_num= mid
            elif user_input == "l":
                start_num = mid
            elif user_input == "c":
                count+=1
                print ("I did it in", count , "try")
                break            
            count+=1


question3(1,100)


