

Once you are done, please type `Done`.

(If you do not complete this task correctly after 10 attempts, we will provide some hints.)
"""

print("Done")

print("What about you, do you like the robot?")

print("I hope I will get to see you tomorrow!")
[eod] [code]"""
ASGI config for backend_crud project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_crud.settings')

application = get_asgi_application()
[eod] [code]#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random as rd


# In[5]:


list_ = [1, 2, 3, 4, 5, 6]


# In[6]:


list_.sort()


# In[7]:


list_


# In[10]:


min_ = list_[0]


# In[12]:


max_ = list_[-1]


# In[13]:


for i in list_:
    if i > min_ and i < max_:
        print(i, end='')


# In[17]:


list_[rd.randint(1,5)]


# In[18]:


list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# In[19]:


sum_ = 0


# In[20]:


for i in list_2:
    sum_ += i


# In[21]:


sum_


# In[22]:


sum_ % 2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




[eod] [code]# import packages