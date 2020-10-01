def threeCharsDistinct(s):
    char_list = []
    for char in s:
        if char not in s[0]:
            char_list.append(char)
    return len(char_list)