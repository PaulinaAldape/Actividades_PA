#!/usr/bin/env python
# coding: utf-8

# # Actividad 4

# ### 1.Crear una matriz 3x3 con valores de 0 a 8

# In[1]:


import numpy as np


# In[2]:


matriz1=np.reshape(np.array(range(0,9)),(3,3))


# In[3]:


matriz1


# ### 2.Crear una matriz identidad de 6x6

# In[7]:


matriz_id=np.identity(6, dtype=int)


# In[8]:


matriz_id

