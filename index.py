import random
letters = ["f", "i", "z", "b", "u"]

for x in range(10): 
    num1 = random.randrange(1, 100)
    if(num1 % 3 == 0 and num1 % 5 == 0):
        fizzbuzz = 0
        for x in range(2): 
            print(letters[fizzbuzz], end="")
            fizzbuzz += 1
        for x in range(2): 
            print(letters[fizzbuzz], end="")
        fizzbuzz += 1
        print(letters[fizzbuzz], end="")
        fizzbuzz += 1
        print(letters[fizzbuzz], end="")
        fizzbuzz = 2
        for x in range(2): 
            print(letters[fizzbuzz], end="")
    elif(num1 % 3 == 0 and num1 % 5 != 0): 
        fizz = 0
        for x in range(2): 
            print(letters[fizz], end="")
            fizz += 1
    elif(num1 % 3 != 0 and num1 % 5 == 0): 
        buzz = 3
        print(letters[buzz], end="")
        buzz += 1
        print(letters[buzz], end="")
        buzz = 2
        for x in range(2): 
            print(letters[buzz], end="")
    else:
        print(num1)