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
    
    # Store last value in a variable
    previous = cur_substring[-1]
    next_c = s[1]
    first_c = cur_substring[0]
    print(first_c, c, next_c, previous)
    
    # Get the min and max of the current string
    min_cur = min(cur_substring)
    max_cur = max(cur_substring)
    
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