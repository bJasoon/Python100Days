#For loops

# fruits = ["Apples", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")


#=====================================

# student_score = [150, 89, 57, 34, 92, 120, 123, 51, 129, 112, 145, 115, 98, 100, 90, 19, 211]

# # total_exam_score = sum(student_score)
# # print(total_exam_score)

# # sum = 0
# # for score in student_score:
# #     sum += score

# # print(sum)

# highest = 0
# for current in student_score:
#     if current > highest:
#         highest = current

# print(highest)

#=====================================

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)

#=====================================
for number in range(1, 101):
    
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")
        continue
    elif (number % 3) == 0:
        print("Fizz")
        continue
    elif (number % 5) == 0 :
        print("Buzz")
        continue
    else:
        print(number)