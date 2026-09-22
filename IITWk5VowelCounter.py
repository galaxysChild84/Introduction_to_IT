#This program is to count the number of vowels in a user input string using a for loop.
input_string_sentence = input("Please enter a sentence:" )
vowel_count = 0
for char in input_string_sentence:
    if char.lower() in 'aeiou':
        vowel_count += 1
print("The number of vowels in", input_string_sentence, "is:", vowel_count)
