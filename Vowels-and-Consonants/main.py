#
# Sam
# 4/23/26
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 


# main function
def main():
    # Get a string from the user.
    user_str = input('Enter a string of characters: ')

    # Report the vowels and consonants.
    print('That string has', num_vowels(user_str), 'vowels and', \
    num_consonants(user_str), 'consonants.')

# The num_vowels function returns the number of
# vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize an accumulator.
    v_count = 0

    # Count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    return v_count
if __name__ == "__main__":
    main()