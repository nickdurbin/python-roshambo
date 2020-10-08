import math

def additionWithoutCarrying(param1, param2):
    # Create a variable to store the final sum
    results = 0
  
    # variable to maintain place value 
    multiplier = 1
  
    # variable to maintain each digit sum 
    bit_sum = 0
  
    # Add numbers till each number becomes zero 
    while (param1 or param2): 
        # Add each bits 
        bit_sum = ((param1 % 10) + (param2 % 10))  
        # Neglect carry 
        bit_sum = bit_sum % 10
          
        # Update result 
        results = (bit_sum * multiplier) + results
        param1 = math.floor(param1 / 10) 
        param2 = math.floor(param2 / 10) 
          
        # Update multiplier 
        multiplier = multiplier * 10
      
    return results