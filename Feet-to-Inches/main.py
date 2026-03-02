#
# Name
# Date
# Feet to inches programing project
# COSC 1010
 


# Function that converts feet to inches
def feet_to_inches(feet):
    return feet * 12


# Main program
def main():
 user_feet = float(input("Enter number of feet: "))
 inches = feet_to_inches(user_feet)
 print("That is", inches, "inches.")


# Call main
main()
