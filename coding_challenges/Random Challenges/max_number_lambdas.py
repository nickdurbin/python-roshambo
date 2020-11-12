def csMaxNumberOfLambdas(text):
  num_of_times = 0
  num_l = text.count("l")
  num_a = text.count("a")
  num_m = text.count("m")
  num_b = text.count("b")
  num_d = text.count("d")
  
  are_equal = False
  if num_m and num_b and num_d == num_l:
    are_equal = True
  
  if are_equal == True:
    if num_a == num_l * 2:
        num_of_times = num_l
  
  return num_of_times