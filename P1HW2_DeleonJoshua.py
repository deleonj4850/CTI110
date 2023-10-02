# Amount of expenses for travel

# 01 OCT 2023

# CTI-110 P1HW2 - Travel Expense

# Deleon_Joshua

#
budget = 2500
location = ('Dallas')
gas = 300
hotel = 700
food = 400

print('This program calculates and displays travel expenses')
print()
print('Enter Budget:', budget)
print()
print('Enter your travel destination:', location)
print()
print('How much do you think you will spend on gas?', gas)
print()
print('Approximately, how much will you need for accomodation/hotel?', hotel)
print()
print('Last, how much do you need for food?', food)
print()
print('----------Travel Expenses----------')
print('Location:', location)
print('Intial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print()
print('Remaining Balance:', budget - (gas + hotel + food))
