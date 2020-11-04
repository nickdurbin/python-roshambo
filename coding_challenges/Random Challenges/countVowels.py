def countVowelConsonant(s):
    
    count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
        else:
            count += 2
    return count
