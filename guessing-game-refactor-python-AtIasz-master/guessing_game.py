import math
import random
a = []
n=0
while n!=10:
    a.append(random.randint(1, 99))
    try:
        g = int(input(f"Enter an integer from 1 to 99 ({n+1}. number): "))
    except ValueError:
        print("I only accept numbers!")
        continue
    while a[n] != g:
        if g < a[n]:
            print("guess is low")
            try:
                g = int(input(f"Enter an integer from 1 to 99: "))
            except ValueError:
                print("I only accept numbers!")
                continue
        elif g > a[n]:
            print("guess is high")
            try:
                g = int(input(f"Enter an integer from 1 to 99: "))
            except ValueError:
                print("I only accept numbers!")
                continue
        else:
            break
    print("you guessed it!")
    n+=1
b = []
n=0
while n!=10:
    b.append(random.randint(1, 49))
    try:
        g = int(input(f"Enter an integer from 1 to 49({n+1}. number): "))
    except ValueError:
        print("I only accept numbers!")
        continue
    while b[n] != g:
        if g < b[n]:
            print("guess is low")
            try:
                g = int(input("Enter an integer from 1 to 49: "))
            except ValueError:
                print("I only accept numbers!")
                continue
        elif g > b[n]:
            print("guess is high")
            try:
                g = int(input("Enter an integer from 1 to 49: "))
            except ValueError:
                print("I only accept numbers!")
                continue
        else:
            break
    print("you guessed it!")
    n+=1