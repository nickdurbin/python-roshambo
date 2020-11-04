'''
  Given a string, remove adjacent duplicate characters.

Example

For s = "aaaaa", the output should be
removeAdjacent(s) = "a";
For s = "abccaaab", the output should be
removeAdjacent(s) = "abcab".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing lowercase English letters only.

Guaranteed constraints:
0 ≤ s.length ≤ 106.

[output] string

A new string with adjacent duplicates removed.
'''

def removeAdjacent(s):
    # Create a list to hold our list of strings
    output = []
    # Variable of our current substring
    cur_substring = ""
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
        if abs(ord(c) - ord(previous)) != 0:
            cur_substring += c
    # Clean up to return any leftover characters
    if cur_substring: 
        output.append(cur_substring)
    # Return our output list length 
    print(f"output: {output}", f"cur_string: {cur_substring}")
    return cur_substring