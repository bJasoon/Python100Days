def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        return True
    else:
        return False
    # Write your code here. 
    # Don't change the function name.

print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2400))
print(is_leap_year(1989))