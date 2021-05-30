#!/usr/bin/env python
# coding: utf-8

# In[3]:


fruit =["apple"]
apple=["apple1","apple2","apple3","apple4"]
fruit.append(apple)
print(fruit)


# In[24]:


keys=("name","school","gender")
values=["malak"]
answer = dict.fromkeys(x,y)
print(answer)


# In[21]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.get("school"))


# In[9]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.items())


# In[10]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.keys())


# In[11]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.pop("name"))


# In[12]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.popitem())


# In[13]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.setdefault("name"))


# In[15]:


#anotherexample
details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.setdefault("anothername","racheal"))


# In[17]:


details={
        "name":"malak",
        "school":"unilag",
        "sex":"female"
}
print(details.update({"nationality":"nigerian"}))


# In[18]:


print(details.values())


# In[ ]:




