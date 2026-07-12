
# detrmine the ticket price based on the age
age = int(input("Enter your age: "))
if age < 5:
    print("Ticket price is free.")
elif age <= 17:
    print("Ticket price is $10.")
elif age <= 65:
    print("Ticket price is $20.")
else:
    print("Ticket price is $15.")
