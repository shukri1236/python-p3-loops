
#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()    

def square_integers(int_list):
    # code goes here!
    square_list = [x ** 2 for x in int_list]
    return square_list

result = square_integers([1, 2, 3, 4, 5])
print(result)



def fizzbuzz():
    # code goes here!
    for number in range(1, 101): 
        if number % 3 == 0 and number % 5 == 0:
           print("FizzBuzz")
        elif number % 3 == 0:
           print("Fizz")
        elif number % 5 == 0:
           print("Buzz")
        else:
           print(number)

fizzbuzz()
    
    