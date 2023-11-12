

# CTI-110
# P4HW2 - Salary Calculator
# Deleon_Joshua
# 12 NOV 2023

total_empl = 0
total_reg_pay = 0.0
total_overtime_pay = 0.0
total_gross_pay = 0.0
overtime_hours = 0


while True:
        empl_name = input("Enter employee's name or 'None' to terminate: ")
        if empl_name.lower() == 'none':
                break
        
        hours_worked = float(input(f"How many hours did {empl_name} work? "))
        pay_rate = float(input(f"What is {empl_name}'s pay rate? "))
        
        if hours_worked <= 40:
                reg_pay = hours_worked * pay_rate
                overtime_pay = 0
	
        else:
                reg_pay = 40 * pay_rate
                overtime_hours = hours_worked - 40
                overtime_pay = overtime_hours * (pay_rate * 1.5)

gross_pay = reg_pay + overtime_pay

total_empl += 1
total_reg_pay += reg_pay
total_overtime_pay += overtime_pay
total_gross_pay  += gross_pay

print(f"Employee name: {empl_name}\n")
print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
print("-" * 90)
print(f"{hours_worked:.1f}\t\t${pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t"
      f"${overtime_pay:.2f}\t\t${reg_pay:.2f}\t\t${gross_pay:.2f}\n")
      
print(f"Total number of employees entered: {total_empl}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_reg_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
