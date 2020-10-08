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
    results  = ""
    for char in string:
        if 65 <= ord(char) and ord(char) <= 90:
            lowercase = ord(char) + 32
            char = chr(lowercase)
        results += char

    return results

print(to_lower_case("LowerCase"))