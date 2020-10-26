'''
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

'''

def checkBlanagrams(word1, word2):
    # Check to see if the same
    # Return False
    if word1 == word2:
        return False
    
    # Grab length to see if they are the same   
    s1 = len(word1)
    s2 = len(word2)
    
    # If not the same length return False
    if s1 != s2:
        return False
    
    # Sort to evaluate each character
    st1, st2 = sorted(word1), sorted(word2)
    
    diff_set = set()
    # For loop to check each character against the adjacent word    
    for i in range(0, s1):
        if st1[i] not in st2:
            diff_set.add(st1[i])
        elif st2[i] not in st1:
            diff_set.add(st2[i])
        # elif st1[i] != st1[2]:
        #     diff_set.add(st1[i])
    
    print(diff_set)
    if len(diff_set) == 1 or len(diff_set) == 2:
        return True
    else:
        return False