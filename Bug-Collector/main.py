#
# sam
# 2/19/2026
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
total = 0

# Get the number of bugs collected each day using a for loop
total = 0 # initialize total once, outside the loop
for day in range(1, 8): # day = 1 to 7
 bugs = int(input(f"Enter the bugs collected on day {day}: ")) # convert input to number
total += bugs # add to total

print(f"You collected a total of {total} bugs.") # prints the correct total