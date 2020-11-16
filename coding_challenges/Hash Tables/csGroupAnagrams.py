'''
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]
Example 2:

Input:
strs = [""]

Output:
[[""]]
Example 3:

Input:
strs = ["a"]

Output:
[["a"]]
Notes:

strs[i] consists of lower-case English letters.
[execution time limit] 4 seconds (py3)

[input] array.string strs

[output] array.array.string
'''

from collections import defaultdict

def csGroupAnagrams(strs):
  # Solution from reading Geeks
  # DefaultDict is a collection built in to Python
  # It is a custom DS and we pass it list and hold it in a var
  temp_list = defaultdict(list)
  # Iterate over our list of words
  for el in strs:
      # Sort and append to our temporary list
      temp_list[str(sorted(el))].append(el)
  # Put all of the values from the temp into a sorted list
  sorted_array = list(temp_list.values())

  return sorted_array


# list comprehension answer
# using list comprehension + sorted() + lambda + groupby()
# Grouping Anagrams
# from itertools import groupby
# temp = lambda test_list: sorted(test_list)
# res = [list(val) for key, val in groupby(sorted(test_list, key = temp), temp)]

# Solution 3
#def createAnagramKey(string):
#     key = ''
#     for ch in sorted(string):
#         key += ch
#     return str(key)
 
 
# def groupAnagramWords(data):
#     group = dict()
#     for ele in data:
#         if group.get(createAnagramKey(ele)) == None:
#             group[createAnagramKey(ele)] = [ele]
#         else:
#             group[createAnagramKey(ele)].append(ele)
#     return group
 
 
# anagram_grouped = groupAnagramWords(data)