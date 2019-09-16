#cerner_2^5_2019
# function to check if substring is present in a string or not  
def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("NO") 
    else: 
        print("YES") 
            
# driver code 
fullString =input("Enter full string:")
subString =input("Enter substring:")
check(fullString, subString)




