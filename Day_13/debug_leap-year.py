def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: #bug was here, 400 was set to 4000
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap(2100))