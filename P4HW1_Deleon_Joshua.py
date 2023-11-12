# CTI-110

# P4HW1 - Score List

# Deleon_Joshua

# 12 NOV 2023

#
num_scores = int(input("How many scores do you want to enter?"))
scores = []

for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
               scores.append(score)

            else:
                print("INVALID Score entered!!!! \nScore should be between 0 and 100")
        except ValueError:
            print("Enter score # again: ")
        
                    
                
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

if 90<= average_score <= 100:
    grade = "A"
elif 80 <= average_score < 90:
    grade = "B"
elif 70 <= average_score < 80:
    grade = "C"
elif 60 <= average_score < 70:
    grade = "D"
else:
    grade = "F"

print('------------------Results------------------')
print(f"Lowest Score: {lowest_score}")
print("Modified List:",scores)
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {grade}")
print('-------------------------------------------')
