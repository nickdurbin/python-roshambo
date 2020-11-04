def mergeStrings(s, t):
  if not (s and t):
    return s + t
  return s[0] + t[0] + mergeStrings(s[1:], t[1:])


s = "aaaaaa"
t = "bbb"

print(mergeStrings(s, t))