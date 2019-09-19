#cerner_2^5_2019
#Find smallest number in created list
sampleList = []
while True:
    element =input("Enter element into the list/press enter to exit ")
    if (element==''):
        break
    sampleList.append(element)
  
sampleList.sort() 
  
print("Smallest element is:", *sampleList[:1])




