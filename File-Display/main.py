#
# sam
# 3/17/26
# File Display Programming Projecint
# COSC 1010
#
# Use comments liberally throughout the program. 
# Open the file 
myfile = open('numbers.txt', 'r')

# Read and disply  the file's contents.
for line in myfile:
    number =int(line)
    print(number)

# Close the file.
myfile.close()