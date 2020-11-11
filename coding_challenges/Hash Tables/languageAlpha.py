"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str
    Output:
    bool
    """
    # UNDERSTAND
    # Plan
    # compare pairs of words to make sure word 1 < word 2
        # compare every letter in each word to the alphabet and then compare them to each other to determine if the order is correct
    # each letter in the new alphabet needs a numeric value so we know what comes first, second, etc. --> dict (hash table)
    # Step 1: map each letter to numeric value in store in dict
    # Step 2:
        # iterate through words and compare pairs of words to see if they're in sorted order
            # compare the first letters.
            # if they're different, we know which one comes first / second.
            #  if they're the same, compare the next two letters,
            #  repeat.
        # if not, return false
    # Step 3: return true
# Dictionary comprehension:
# alpha = "abcdefg"
# dictionary = {character: alpha.index(character) for character in alpha}
# d2 = {}
# for character in alpha:
#     d2[character] = alpha.index(character)

