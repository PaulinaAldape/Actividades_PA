#!/usr/bin/env python
# coding: utf-8

# # Actividad 8

# ### 1. Hagamos un programa que determine si eres mayor de edad o no y el genero.

# ### Básica

# In[ ]:


edades=[13,14,18,22,23,8,20]


# In[ ]:


for i in edades:
    if i>=18:
        print(i,"Mayor de edad")
    else:
        print(i,"Menor de edad")


# ### Avanzada

# In[28]:


diccionario={13:"F",14:"M",18:"M",22:"F",23:"F",8:"M",20:"F"}


# In[39]:


for k,v in diccionario.items():
    if k>=18:
        print("Es mayor de edad tiene: ",k," ","El genero es: ",v)
    else:
        print("Es menor de edad tiene: ",k," ","El genero es: ",v)


# In[ ]:




