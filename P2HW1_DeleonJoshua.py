# Amount of expenses for travel

# 15 OCT 2023

# CTI-110 P2HW1 - Travel

# Deleon_Joshua

#
budget = float(input('Enter your budget: '))
location = input('Enter your travel destination: ')
gas = float(input('Enter the amount you will spend on gas: '))
hotel = float(input('Enter the amount you will spend on accomodation: '))
food = float(input('Enter the amount you will spend on food: '))

print('This program calculates and displays travel expenses')
print()
print('Budget:', budget)
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
print('\nLocation:         ', location)
print('Intial Budget:     $', budget)
print('Fuel:              $', gas)
print('Accomodation:      $', hotel)
print('Food:              $', food)
print('-----------------------------------')
print()
print()
print('Remaining Balance: $', budget - (gas + hotel + food)) 
