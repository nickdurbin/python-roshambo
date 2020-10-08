def increasingSubstrings(s):
    # Overall runtime: O(n)
    # PLAN
    output = []
    cur_substring = ""
    # iterate through s character by character
    for c in s:             # O(n) (n = len(s))
        # compare the current character to the previous character (or the last char in cur_substring)
        if cur_substring == "":
            cur_substring = c
            continue
        previous = cur_substring[-1]   # O(1)
        # if it's increasing
        if is_increasing(previous, c):  # O(1)
            # then it's part of the same substring, append to cur substring
            cur_substring += c
        # else 
        else: 
            # we append cur_substring to our output list
            output.append(cur_substring)    # O(1)
            # and we have to start a new cur_substring with the current character. 
            cur_substring = c
    if cur_substring: 
        output.append(cur_substring)
    # return our output list
    return output
def is_increasing(char1, char2): # O(1)
    lower = "abcdefghijklmnopqrstuvwxyz" # O(1)
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char1_index = lower.find(char1) # O(n) where n = len(lower) = 26 --> O(26) --> O(1)
    char2_index = lower.find(char2)
    if char1_index == -1: 
        char1_index = upper.find(char1)
        char2_index = upper.find(char2)
    # if the index of char2 == index of char1 + 1:
    return char2_index == char1_index + 1

# Notes
# Use python built in char() and ord() methods 
# To check if list elements are alphanumeric
# And in sequencial order 

# Need to iterate through the loop and check the alpha code between 2 elements
# If they are in sequencial order, ADD them to the same string (concatenate)
# If they are not end the first string and start a second string
# Repeat the process till we hit the end of the list
# Return the list.

# function increasingSubstrings(s) {
#     const return_array = [];
#     let base_pointer = 0;
#     for( i = 0; i < s.length; i++){
#         if( s.length < 2 ) return [s[i]];
#         if( s.charCodeAt( i + 1 ) !== s.charCodeAt(i) + 1 ){
#             return_array.push( s.slice(base_pointer, i + 1) );
#             base_pointer = i + 1;
#         }
#     }
#     return return_array;
# }