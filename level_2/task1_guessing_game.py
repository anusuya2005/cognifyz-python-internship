import random
guess_num=random.randint(1,100)
count=0
while True:
    count+=1
    num=int(input("Guess number between 1 to 100 :"))
    if num>guess_num:
        print("Too high")
    elif num<guess_num:
        print("Too low")
    else:
        print("you have guessed the correct number")
        print("you guessed in",count,"attempts")
        break
    
