'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.
'''

def first_not_repeating_character(s):
  # list to keep character order
  char_list = []
  
  # Dictionary to keep our key and value
  char_dict = {}
  
  # iterate over our string
  for char in s:
    # If this character already exists in our dictionary add to its count
    if char in char_dict:
      char_dict[char] += 1
    # Else add to dictionary and start count at 1
    else:
      char_dict[char] = 1 
      char_list.append(char)
  # iterate over our list of characters
  for char in char_list:
    # If the value == 1 
    # This will be the first non repeating char
    # Return it or else return the '_'
    if char_dict[char] == 1:
      return char
  return '_'