#!/usr/bin/env python
# coding: utf-8

# In[8]:


#cerner_2^5_2019

#Sample Bar Chart using Matplotlib
import matplotlib.pyplot as plt
plt.bar([2,4,6,8,10],[5,2,7,8,2], label="Case 1", color='g')
plt.bar([1,3,5,7,9],[8,6,2,5,6], label="Case 2", color='r')

plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis:Height')
plt.title('Sample Bar chart using Python')

plt.show()


# In[ ]:




