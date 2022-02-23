
print("Welcome to Split My Pizza")

print("How many slices would you like on your pizza?")
pizza_slices = int(input())
print("How many people are sharing?")
people = int(input())

Slices = pizza_slices // people
remaining_slices = pizza_slices % people

print(f"There are going to be {Slices} slices per person")
print(f"There are going to be {remaining_slices} remaining slices")

print("What is the bill total?")
bill_total = float(input())
print("What tip percentage would you like to leave?")
tip_percentage = int(input())

percentage_decimal = tip_percentage / 100
tip_total = bill_total * percentage_decimal
bill_total = bill_total + tip_total

cost_per_person = bill_total / people

print(f"Total bill including tip is £{bill_total}")
print(f"Total cost per person is £{cost_per_person}")

print("Thank you for using Split My Pizza")
