# Program: Count The Vowels In A String.


# Returns the number of vowels in the string 
def count_vowels(text):
  
  count = 0
  
  for character in text:
    if (character in "aAeEiIoOuU"):
      count += 1

  return count 

# Prompt the user to enter in a string, store the string entered into 'text'
text = input("Enter your text: ")

# Call the count_vowels() function with the provided string and store the count
# of vowels returned by the function into count.
count = count_vowels(text)

print("Total vowel count : ", count)
