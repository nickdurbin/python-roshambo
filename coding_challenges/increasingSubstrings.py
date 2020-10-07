import string

def increasingSubstrings(s):
    # Put the elements into a list in smallest form
    s = list(s)
    # Possibly create an array to move elements from one to the other.
    big_arr = []
    print(s)
    # Create a for loop to iterate over each element in the list
    for i in range(len(s) - 1):
        # Convert variables to numeric alpha
        # Save the first item in the index in a variable
        first_el = ord(s[i])
        #Save the second item in the index in a variable
        second_el = ord(s[i+1])
        # While loop to keep checking if the first element is lower
        # which is flawed because we need to check explicit order
        # but for now, if lower concatenante and add to new list
        while first_el < second_el:
            first_el += second_el
            big_arr.append(first_el)
            # If first element is larger or of equal value
            # Start a new string and the process over
            if first_el >= second_el:
                big_arr.append(first_el)
            else: 
                pass
            
    print(s, big_arr)
    return big_arr

# Notes
# Use python built in char() and ord() methods 
# To check if list elements are alphanumeric
# And in sequencial order 

# Need to iterate through the loop and check the alpha code between 2 elements
# If they are in sequencial order, ADD them to the same string (concatenate)
# If they are not end the first string and start a second string
# Repeat the process till we hit the end of the list
# Return the list.