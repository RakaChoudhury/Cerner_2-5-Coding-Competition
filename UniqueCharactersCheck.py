#cerner_2^5_2019
def check_unique_characters(input_str): 
   
    if len(input_str) > 256: 
        return False
  
    char_list = [False] * 128
  
    for i in range(0, len(input_str)): 

        val = ord(input_str[i]) 
        if char_list[val]: 
            return False
  
        char_list[val] = True
  
    return True
  
input_str = input("Enter string for which you want to verify if all characters are unique or not:")
print(check_unique_characters(input_str)) 

