#
# sam
# 1/2/26
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Everything inside the function is indented 4 spaces (one tab)

def main():
    total = 0
    count = 0
    try:
        with open('numbers.txt', 'r') as myfile:
            for line in myfile:
                try:
                    number = int(line)
                    total += number
                    count += 1
                except ValueError:
                    print(f"Skipping invalid data: {line.strip()}")

        if count > 0:
            average = total / count
            print(f"The average of the numbers is: {average}")
        else:
            print("The file was empty or contained no valid numbers.")

    except IOError:
        print("Error: Could not read 'numbers.txt'. Please check if the file exists.")

if __name__ == "__main__":
    main()
