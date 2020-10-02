def threeCharsDistinct(s):
    # abcdaaae
    # abc --> all distinct
    # bcd --> all distinct
    # cda --> all distinct
    # daa --> not all distinct
    num_distinct = 0
    # keep a count of num distinct triplets
    # iterate through the characters in s: 
    for i in range(0, len(s) - 2): 
        # get the triplet
        substring = s[i:i+3]
        print(i, i+3, substring)
        # check if they're all distinct
        # check the count of each character
        substring_chars = set(substring)
        print(substring_chars)
        if len(substring_chars) == 3: 
            num_distinct += 1
        # counts = {} # character --> counts
        # for c in substring: 
        #     if c in counts: 
        #         counts[c] += 1
        #     else: 
        #         counts[c] = 1
        # for c, count in counts.items(): 
        #     distinct = True
        #     if count > 1:
        #         distinct = False
        # if distinct = True: 
        #     num_distinct += 1 
                # increment num distinct triplets
    return num_distinct