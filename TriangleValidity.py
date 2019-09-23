#cerner_2^5_2019
#Check if a triangle of positive area is possible with the given angles 
  
def isTriangleExists(a, b, c): 
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 
        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 
            return "YES"
        else: 
            return "NO"
    else: 
        return "NO"

a = input("Enter first angle") 
b = input("Enter second angle") 
c = input("Enter third angle") 
  
print(isTriangleExists(int(a), int(b), int(c))) 