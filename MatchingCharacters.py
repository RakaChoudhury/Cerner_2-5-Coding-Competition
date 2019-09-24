#cerner_2^5_2019
#Count number of matching characters in a pair of strings   
def count(input1, input2):  
    count, j = 0, 0
    for i in input1:     
        if input2.find(i)>= 0 and j == input1.find(i):  
            count += 1
        j += 1
    print ('Number of matching characters are : ', count) 
  
def main():  
    input1 = input("Enter first string")
    input2 = input("Enter second string")
    count(input1, input2)  

if __name__=="__main__": 
    main() 