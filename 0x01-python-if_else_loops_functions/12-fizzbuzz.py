#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i == 1:
            print("{}".format(i), end="")
        elif i % 3 == 0:
            print(" Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
        elif i % 5 == 0:
            print(" Buzz", end="")
        else:
            print(" {}".format(i), end="")
    print("")
