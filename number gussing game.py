import random
ans=random.randint(1,100)
while True:
    num=int(input("enter a number fron 1 to 100:"))
    if(num>=1 and num<=100):
        if num>ans:
            print("it is high!")
        elif num<ans:
            print("it is low!")
        else:
            print("yes you guessed!")
            break
    else:
        print("invalid!")