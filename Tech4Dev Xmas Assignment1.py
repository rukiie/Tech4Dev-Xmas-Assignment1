#!/usr/bin/env python
# coding: utf-8

# # Check at list 20 methods in list, tuples, dictionaries, and give an example  writing a python code.

# # LIST

# In[55]:


#1 - append


# In[56]:


# Add Rukayat to the list
classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
classE.append("Rukayat")
print (classE)


# In[57]:


#2 - remove


# In[58]:


# remove "Mercy" from the list
classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
classE.remove("Mercy")
print (classE)


# In[59]:


#3 - clear


# In[60]:


# To  empty the list
classE.clear()
print (classE)


# In[61]:


#4 - copy


# In[62]:


# TO copy and remove an element from the list
classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
copy_classE = classE.copy()
copy_classE.remove("Folashade")
print(classE)
print(copy_classE)


# In[63]:


# TO copy and add an element from the list
classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
copy_classE = classE.copy()
copy_classE.append("Titilayo")
print(classE)
print(copy_classE)


# In[64]:


# TO copy, remove, and replace an element from the nested parenthesis list
classE = ["Stephenie", ["Juliet","Claudia"],"Mercy","Folashade","Lynda"]
copy_classE = classE.copy()
copy_classE.remove("Folashade")
copy_classE[1][1] = "Ganiyat"
print(classE)
print(copy_classE)


# In[11]:


#5 - count


# In[12]:


# count the occurance an item in an array/list
classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda", "Mercy", "Claudia","Mercy"]
Mercys = classE.count("Mercy")
print (Mercys)


# In[13]:


Juliet = classE.count("Juliet")
print (Juliet)


# In[14]:


Juliet = classE.count("Apple")
print (Juliet)


# In[15]:


#6 - extend


# In[16]:


classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
classE2 =["Claudia","Rukayat","Titilayo","Ganiyat", "Alex"]
classE.extend(classE2)
print (classE)


# In[17]:


#7 - index()


# In[18]:


classE = ["Stephenie", "Juliet","Mercy","Folashade","Lynda"]
print (classE.index("Folashade"))


# In[19]:


print (classE.index("Lynda"))


# In[20]:


print (classE.index("Stephenie"))


# # TUPLES

# In[21]:


#8 - len


# In[22]:


# To know the length of the items in the tuple i.e how many element is present in the tuple.
t = (12,18,22,54,87,14,2,76,55,43,18,65,100,16,73,18,6,105,14,29,18,14,99,30,12)
print(len(t))


# In[23]:


#9 - max


# In[24]:


# To find the maximum num present inside the tuple
print(max(t))


# In[25]:


#10 - min


# In[26]:


# To find the minimum num present inside the tuple
print(min(t))


# In[27]:


#11 - sum


# In[28]:


# To calculate sum/ addition of all element of the tuple
print(sum(t))


# In[29]:


#12 - index


# In[30]:


# To find the index of element 105
print (t.index(105))


# In[31]:


#13 - count


# In[32]:


# TO know/count how many times a particular element is present in a tuple
print(t.count(18))


# In[33]:


#14 - Sorted


# In[34]:


# To sort the element in the turple 
print(sorted(t))


# # Dictionary

# In[35]:


#15 - get


# In[36]:


# To get the corresponding value of key "Lynda"
group1= {"Stephenie":"Benue", "Mary":"Kenya", "Fola":"Abeokuta", "Lynda":" Eygpt", "Juliet":"Anambra", "Titilayo":"Osun"}
print(group1.get("Lynda"))


# In[37]:


print(group1.get("Stephenie"))


# In[38]:


print(group1.get("Claudia"))


# In[39]:


# To customise a response to a key-value that is not in the dictionary
print(group1.get("Claudia", "Not Found"))


# In[40]:


#16 - pop


# In[41]:


# To remove a key-value from the dictionary
group1.pop("Juliet")
print(group1)


# In[42]:


#17 - keys


# In[43]:


# To know all the keys present in the dictionary
print(group1.keys())


# In[44]:


#18 - items


# In[45]:


# To get all the elements in the form of tuple
print(group1.items())


# In[46]:


#19 - popitem


# In[47]:


# To by default get the last element from the dictionary
print(group1.popitem())


# In[48]:


#20 - update


# In[49]:


group1 = {"Stephenie":"Benue", "Mary":"Kenya", "Fola":"Abeokuta", "Lynda":" Eygpt", "Juliet":"Anambra", "Titilayo":"Osun"}
group2 = {"Maryam":"Ilorin", "Amira":"Niger",}
group1.update(group2)
print(group1)


# # Classwork 2

# In[50]:


# Print the first 10 natural numbers
for i in range(1,11):
    print(i)


# In[51]:


#print("====The first 10 Natural Numbers====")
print("====The first 10 Natural Numbers====")


# In[52]:


#count the total number of digits in a number
num = (9,8.7,5,4,5,3,6,8,2,5,8,9,5,3,4,2,6,5)
print(len(num))


# In[53]:


# prime numbers
for i in range(1,21):
    
    for n in range(2,i):
        
        if (i % n == 0):
            break
            
    else:
        print(i,end='  ')
    


# In[54]:


num = 6
for i in range (1,13):
    fag = num*i
    print(num, "x",i,"=",fag)

