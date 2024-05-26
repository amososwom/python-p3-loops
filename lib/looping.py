#!/usr/bin/env python3

def happy_new_year():
    count = 10

    while count >= 1:
        print(count)
        if count == 1:
            print("Happy New Year!")
        count -= 1

def square_integers(int_list):
    int_list = [value * value for value in int_list]
    return int_list

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()