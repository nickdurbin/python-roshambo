# 24-hour format using Regular Expression.  
import re 
  
# Function to validate the time  
# in 24-hour format  
def isValidTime(time): 
      
    # Regex to check valid time in 24-hour format.  
    regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$";  
  
    # Compile the ReGex  
    p = re.compile(regex);  
  
    # If the time is empty  
    # return false  
    if (time == "") : 
        return False; 
          
    # Pattern class contains matcher() method 
    # to find matching between given time  
    # and regular expression. 
    m = re.search(p, time); 
      
    # Return True if the time 
    # matched the ReGex otherwise False 
    if m is None : 
        return False; 
    else : 
        return True

# import time as timer
        
# def validTime(time):
#     try:
#         timer.strptime(time, '%H:%M')
#         return True
#     except ValueError:
#         return False