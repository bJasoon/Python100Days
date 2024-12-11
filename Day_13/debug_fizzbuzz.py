# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: #bug was here, set to or instead of and
            print("FizzBuzz")
        elif number % 3 == 0: # bug was here until line 8, was set to individual ifs instead of elifs
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number) #bug was here. number was encased in []

fizz_buzz(30)