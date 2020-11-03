"""
Given a string, implement a function that returns the string with all lowercase
characters.
Example 1:
Input: "LambdaSchool"
Output: "lambdaschool"
Example 2:
Input: "austen"
Output: "austen"
Example 3:
Input: "LLAMA"
Output: "llama"
*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    # UNDERSTAND
    #
    # Plan
    # A = 65
    # a = 97
    # to convert from uppercase to lowercase, we can add 32 to the int representation
    # -- convert back from the decimal representation to the character
    # make a result string, initialize to empty
    result = ""
    # iterate through the string
    for c in string:
    #   if ord(c) is between 65-90:
        if 65 <= ord(c) and ord(c) <= 90:    # ord takes character and turns it to decimal representation
            # we need to convert to lower case
            lowercase = ord(c) + 32
            c = chr(lowercase)  # chr is the opposite of ord. turn decimal back to character
    #   otherwise, just move on
    #   in both cases, we need to append the character to the result string
        result += c
    return result
print(to_lower_case("LowerCAse"))