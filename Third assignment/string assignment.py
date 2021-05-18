#!/usr/bin/env python
# coding: utf-8

# In[ ]:


find method: it returns the index position of a character in a string


# In[1]:


school="University of lagos"
print(school.find("n"))


# In[ ]:


count method:It returns the number of times the characters appear in a string


# In[2]:


name="Malak"
print(name.count("a"))


# In[ ]:


index method: This string method returns the index position of a character in a string, but returns an error if the character is not present in the string
    


# In[3]:


school="University of lagos"
print(school.index("t"))


# In[4]:


school="University of lagos"
print(school.index("m"))


# In[ ]:


upper method: This method capitalizes all the characters of a string


# In[7]:


name="Malak is a smart girl"
print(name.upper())


# In[ ]:


title method: It changes the  first characters of a string in a sentence to upper case


# In[8]:


name= "malak is a smart girl"
print(name.title())


# In[ ]:


capitalize method: The method capitalizes the first character of the first word


# In[9]:


name="malak"
print(name.capitalize())


# In[ ]:


swapcase method: This method changes the characters that are uppercase to lowercase and those that are lowercase to uppercase
    


# In[10]:


sentence= "This is going to be a Good Day"
print(sentence.swapcase())


# In[ ]:


replace method: Thos method replaces a character of a string with another


# In[12]:


name="Malak"
print(name.replace("a","i"))


# In[ ]:


startwith method:it returns a true or false value to check if a string starts with a particular letter


# In[ ]:


name="malak"
print(name.startswith("m"))


# In[ ]:


endswith method: this method returns a true or false checking if the string endswith  a certain character


# In[14]:


gender="female"
print(gender.endswith("y"))


# In[ ]:


isalpha: This method checks if a string is made up of alphabets, and returns a true or false


# In[23]:


gender="female"
print(gender.isalpha())


# In[ ]:


isupper: this method returns a "True", if the string is made up of uppercase characters


# In[24]:


gender="female"
print(gender.isupper())


# In[ ]:


islower: This method also checks if all the characters in a string are made up of lowercase letters.


# In[25]:


gender="Female"
print(gender.islower())


# In[ ]:




