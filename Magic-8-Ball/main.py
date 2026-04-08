#
# sam
# 4/8/2026
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random

def main():
    responses = []

    # this part reads your text file into a list
    infile = open('8_ball_responses.txt', 'r')
    for line in infile:
        responses.append(line.strip())
    infile.close()

    keep_going = 'y'
    while keep_going.lower() == 'y':
        input('Ask the Magic 8 Ball a yes/no question: ')

    # this picks a random answer from your file
        print(random.choice(responses))

        keep_going = input('\nDo you have another question? (y/n): ')

# this is the "start button" that tells python to run the main function
if __name__ == '__main__':
    main()