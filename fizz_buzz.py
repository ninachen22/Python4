num = int

def fizz(num):
    if num % 3 == 0:
        return True
    else: 
        return False

def buzz(num):
    if num % 5 == 0:
        return True
    else: 
        return False

def fizz_buzz():
    for i in range (1, 101):
        if fizz(i) and not buzz(i):
            print("Fizz")
        elif buzz(i) and not fizz(i):
            print("Buzz")
        elif fizz(i) and buzz(i):
            print ("FizzBuzz")
        else: print (i)

fizz_buzz()

