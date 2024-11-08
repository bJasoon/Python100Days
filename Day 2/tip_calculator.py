print("welcome to the Tip Calculator!")

totatBill = float(input("What was the total bill?\n$"))
tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
peopleSplit = int(input("How many people will split the bill?\n"))
eachBill = round(((totatBill * ((tipPercentage / 100) + 1)) / peopleSplit), 2)

print(f"Each person will pay: ${eachBill}")