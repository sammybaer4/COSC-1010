#
# sam
# 2/19/2026
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
budget = float(input("Enter the amount budgeted for the month: "))

# Initialize total expenses
total_expenses = 0.0

# Ask how many expenses they will enter
num_expenses = int(input("How many expenses will you enter this month? "))

# Loop through each expense
for i in range(1, num_expenses + 1):
 expense = float(input(f"Enter expense #{i}: $"))
total_expenses += expense

# Calculate difference
difference = budget - total_expenses

# Display results
print(f"\nBudget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")

if difference >= 0:
 print(f"You are ${difference:.2f} under budget.")
else:
 print(f"You are ${-difference:.2f} over budget.")