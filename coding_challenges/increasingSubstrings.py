def increasingSubstrings(s):
  s = list(s)
  big_arr = []
  print(s)
  for i in range(len(s) - 1):
    first_el = ord(s[i])
    second_el = ord(s[i+1])
    if first_el != second_el:
      first_el += second_el
      big_arr.append(first_el)
      first_el = s[i]
    else: 
      big_arr.append(second_el)
          
  print(big_arr)
  return big_arr