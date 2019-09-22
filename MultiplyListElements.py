#cerner_2^5_2019
#Multiply all values in a list using numpy.prod() 
  
import numpy 
sampleList = []
while True:
    element =input("Enter element into the list/press enter to exit ")
    if (element==''):
        break
    sampleList.append(int(element)) 

print(sampleList)
result1 = numpy.prod(sampleList) 
print(numpy.prod(sampleList)) 