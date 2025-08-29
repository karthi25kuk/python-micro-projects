import random as rm

print("enter \"y\" to role dice,\"n\" to stop game.")
while True:
    inp=input("enter a choice:").strip().lower()
    if inp=='y':
        value=rm.randint(1,6)
        print(value)
    elif inp=='n':
        print("thanks for rolling!")
        break
    else:
        print("invalid choice! please try again")