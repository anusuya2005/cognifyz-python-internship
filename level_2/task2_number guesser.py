import random
start_range=int(input("Enter Start Range :"))
end_range=int(input("Enter End range :"))
if start_range>end_range:
    print("Invalid range")
    exit()
guess_num=random.randint(start_range,end_range)
count=0
while True:
    count+=1
    num=int(input(f"Guess number between {start_range} to {end_range} :"))
    if num>guess_num:
        print("Too high")
    elif num<guess_num:
        print("Too low")
    else:
        print("you have guessed the correct number")
        print("you guessed in",count,"attempts")
        break
    
