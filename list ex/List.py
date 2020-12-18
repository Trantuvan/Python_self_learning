#!/usr/bin/env python
# coding: utf-8

# # Exercise 1

# In[ ]:


gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00,
'Television', 1000, 'Laptop Case', 'Camera Lens']

temp = [type(item) for item in gadgets] #tai sao lai can temp


# In[ ]:


strings = [k for k in gadgets if isinstance(k, str) == True]
numbers = [k for k in gadgets if isinstance(k, str) == False]

print(strings)
print(numbers)


# In[ ]:


strings.sort(reverse=True)
print(strings)

numbers = [float(k) for k in numbers]
numbers.sort()
print(numbers)


# # Exercise 2

# In[ ]:


mixed = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
mixed[2][2].append(7000)
print(mixed)


# # Exercise 3

# In[ ]:


scores =  [86,86,85,85,87,85,83,23,45,84,93,86,87] 
first = max(scores)
scores.sort()
temp = [k for k in scores if k != first]
second = temp[-1]
temp = [k for k in scores if k != first and k!= second]
third = temp[-1]
print(second)
print(third)




# # Exercise 4

# In[ ]:


webs = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
webs = [k.split(".")[2] for k in webs]
print(webs)


# # Exercise 5

# In[ ]:


consecutive = [[5*i + j for j in range(1,6)] for i in range(6)]
print(consecutive)


# In[ ]:




