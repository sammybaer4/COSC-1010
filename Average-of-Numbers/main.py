#
# sam
# 3/17/26
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Initialize variables to keep track of the sum and count
total = 0
count = 0

# Open the file
myfile = open('numbers.txt', 'r')

# Loop through the file
for line in myfile:
 number = int(line)
total += number # Add the number to our running total
count += 1 # Increment our count by 1

# Close the file
myfile.close()

# Calculate the average
# We use an if statement just in case the file was empty to avoid a division by zero error
if count > 0:
    average = total / count
    print(f"The average of the numbers is: {average}")
else:
     print("The file was empty.")