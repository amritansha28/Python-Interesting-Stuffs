import random
d=1
while d==1:
    a=random.randint(1,1000)
    print("I have a number between 1 and 1000")
    print("Can you guess my number?")
    print("Please type your first guess.")
    c=1
    while c==1:
        b=int(input())
        if a==b:
            print("Excellent! you guessed the number! Would like to play again (y or n)")
            c=0
            e=input()
            if e=="y":
                None
            else:
                d=0
        elif a>b:
            print("Too low.Try again")
        elif a<b:
            print("Too high.Try again")
        else:
            print("No. out of range!!")
