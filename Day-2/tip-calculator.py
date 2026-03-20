print("Welcome to the tip calculator!")
bill= float(input("what was the total bill? £"))
tip= int(input("What percentage tip would you like to give? 10 12 15"))
people= int(input("How many people to split the bill? "))

ind_bill = (bill/people)* (1+ tip/100)
print(f"each person should pay : £ {round(ind_bill,2)}")

