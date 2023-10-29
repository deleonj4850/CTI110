

# CTI-110
# P3HW2 - Salary
# Deleon_Joshua
# 29 OCT 2023

empl_name = input("Enter employee's name: ")
hours_worked= float(input("Enter number of hours worked: "))
pay_rate= float(input("Enter employee's pay rate: "))

over_time_pay = 0.0
over_time = 0.0
if hours_worked > 40:
	over_time = hours_worked - 40
	ot_pay_rate = pay_rate + (pay_rate * 0.5)
	over_time_pay = over_time * ot_pay_rate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate

gross_pay = reg_pay + over_time_pay

print('-'*36)
print("Employee name: ",empl_name)
print()
print("Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay")
print("----------------------------------------------------------------------------------------------------")
print(hours_worked," \t\t ",pay_rate," \t ",over_time," \t\t ",over_time_pay," \t  $",reg_pay," \t $",gross_pay)
