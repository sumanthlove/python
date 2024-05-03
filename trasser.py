print("Welcome to trasure island your misssion is to find the trasser")
choose1=input("chooose the left are right")
if choose1=="left":
    choose2=input("choose the wait are swim.")
    if choose2=="wait":
        choose3=input("choose the colour yellow ,green and red")
        if choose3=="red":
            print("game over")
        elif choose3=="yellow":
            print("you win")
        elif choose3=="green":
            print("game over")

    else:
        print("end the game")

else:
    print("end the game") 
