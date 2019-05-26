#!/usr/bin/env python
# coding: utf-8

# In[35]:


kk=""
for i in range(0,6):
    k="" 
    for j in range(0,i):
        k+= "*"
    print(k)
K=""
   # print("\n")    


# In[90]:


kk=""
m=6
for i in range(0,m):
    k="" 
    for h in range(0,i):
            k+=" "
    for j in range(0,m-i):
        ll=m-i
        if ll == 0:  
            k+= "*"
        else:
            k+= "**"
    print(k)


# In[92]:


k=2
for h in range(1,11):
    print(k,"*",h,"=",k*h)
    


# In[97]:


k=2
for h in range(1,11):
    for i in range(2,4):
        print(i,"*",h,"=",i*h,end="\t")


# In[ ]:




