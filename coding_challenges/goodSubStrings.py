'''
You're writing a new programming language and you'd like it to have the capability of splitting a string into substrings with limited characters. More specifically, we'll call a substring good if the absolute difference in ASCII codes between any two of its characters is less than or equal to k.

For example, if k = 3, then the string "bad" would be considered good, since the greatest difference in ASCII codes is 3 (between the a and d characters). The string "nice" would not be considered good, since there's a difference of 11 between the c and n characters.

You are given a string strToSplit that consists of lowercase English letters only, and your task is to find the minimal number of good substrings you can split it into.

Hint: Iterate over the string strToSplit and keep the ASCII codes of the smallest and the greatest characters in the current substring. Every time when the difference between them becomes greater than k, it means that the last considered symbol should be the first one in a new substring.

Example

For strToSplit = "aaabaaabb" and k = 0, the output should be goodSubstrings(strToSplit, k) = 4.

strToSplit could be split into ["aaa", "b", "aaa", "bb"]. Each substring must consist of only one type of character, because it is required that |s[i] - s[j]| ≤ 0 for each substring s.

For strToSplit = "aaabaaabb" and k = 1, the output should be goodSubstrings(strToSplit, k) = 1.

Since the only characters in the string have a difference of 1, aaabaaabb meets the requirement |strToSplit[i] - strToSplit[j]| ≤ 1. So only 1 substring is required (and it's the full original string).

For strToSplit = "aaabzaaabb" and k = 10, the output should be goodSubstrings(strToSplit, k) = 3.

strToSplit could be split into ["aaab", "z", "aaabb"]. Since the z character has such a large difference with each of its adjacent characters, it must be in a substring of its own.
'''

def goodSubstrings(strToSplit, k):
  # Create a list to hold our list of strings
  output = []
  
  # Variable of our current substring
  cur_substring = ""
  
  # Make sure our string is lowercase
  s = strToSplit.lower()
  
  # Iterate through the string character by character
  for c in s:
    # compare the current character 
    # to the previous character 
    # or the last char in cur_substring
    if cur_substring == "":
      cur_substring = c
      continue

    # Get the min and max of the current string
    min_cur = min(cur_substring)
    max_cur = max(cur_substring)
    
    # Store last value in a variable
    previous = cur_substring[-1]
    next_c = s[1]
    first_c = cur_substring[0]
    print(first_c, c, next_c, previous)
    
    # if the absolute difference between 2 characters
    # is less than or equal to k
    if abs(ord(c) - ord(previous)) <= k and abs(ord(max_cur) - ord(min_cur)) <= k and abs(ord(c) - ord(first_c)) <= k:
      cur_substring += c
    
    else: 
      # Append cur_substring to our output list
      output.append(cur_substring)
      # Start a new cur_substring with the current character. 
      cur_substring = c
          
  # Clean up to return any leftover characters
  if cur_substring: 
    output.append(cur_substring)
  # Return our output list length 
  print(f"output: {output}", f"cur_string: {cur_substring}")
  return len(output)

print(goodSubstrings("aaadddbbbffffppppz", 4))
print(goodSubstrings("zaaadddbbbffffppppz", 4))


# Time complexity is O(n^2)
# def goodSubstrings(strToSplit, k):
#     # UNDERSTAND
#     # substring is good if absolute difference in ascii code of 2 characters <= k
#     # can use ord to convert from character to ascii code
#     # find the minimal number of good substrings to split it into
#     # substring --> contiguous 
#     # keep a count of the number of substrings
#     count = 0
#     current_substring_ords = []
#     # iterate over strToSplit
#     for c in strToSplit: 
#         # map each character in the current substring to ascii code 
#         current_substring_ords.append(ord(c)) # ord(c) takes c and returns the unicode / ascii code
#         # Find the min and max ords in current_substring_ords because they'll have the biggest difference
#         min_ord = None
#         max_ord = None
#         for c_ord in current_substring_ords: 
#             if not min_ord or c_ord < min_ord:
#                 # if the current ord is less than the min, set the min to be the current ord
#                 min_ord = c_ord
#             if not max_ord or c_ord > max_ord:
#                 max_ord = c_ord
#         # if there are two characters k apart, split
#         if max_ord - min_ord > k:
#             # "splitting" means we "finish" the current substring
#             count += 1
#             # and start a new substring with the current character
#             current_substring_ords = [ord(c)]
#     # add the last substring
#     count += 1
#     return count