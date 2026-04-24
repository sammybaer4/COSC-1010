#
# Name
# Date
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def convert_to_pig_latin(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    pig_latin_words = []

    for word in words:
       if len(word) > 1:
            # Move first character to end and add 'ay'
# word[1:] is everything but the first letter
# word[0] is the first letter
             new_word = word[1:] + word[0] + "ay"
       else:
          # If it's a single letter (like 'I'), just add 'ay'
          new_word = word + "ay"

       pig_latin_words.append(new_word.upper())

    # Join the list back into a single string
    return " ".join(pig_latin_words)

# --- Main Program ---
user_input = input("Enter a sentence: ")
result = convert_to_pig_latin(user_input)

print(f"Pig Latin: {result}")