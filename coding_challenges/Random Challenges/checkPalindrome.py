def checkPalindrome(inputString):
    # I can use the same approach as last question here.
    # I can reverse the string and save it in a variable
    # Then check to see if the 2 are equal.
    # Return appropriate boolean value.
    reverse = inputString[::-1]
    
    return reverse == inputString
