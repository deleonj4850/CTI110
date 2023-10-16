# Amount of expenses for travel

# 01 OCT 2023

# CTI-110 P1HW2 - Travel Expense

# Deleon_Joshua

#
budget = int(input('Enter your budget: '))
destination = input('Enter your travel destination: ')
gas = int(input('Enter the amount you will spend on gas: '))
hotel = int(input('Enter the amount you will spend on accomodation: '))
food = int(input('Enter the amount you will spend on food: '))

print('This program calculates and displays travel expenses')
print()
print('Budget:', budget)
print()
print('Enter your travel destination:', destination)
print()
print('How much do you think you will spend on gas?', gas)
print()
print('Approximately, how much will you need for accomodation/hotel?', hotel)
print()
print('Last, how much do you need for food?', food)
print()
print('----------Travel Expenses----------')
print('Location:', destination)
print('Intial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print()
print('Remaining Balance:', budget - (gas + hotel + food)) 
