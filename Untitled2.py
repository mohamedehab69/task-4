#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Test
# Let's test your knowledge!

# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[ ]:


st = 'Print only the words that start with s in this sentence'


# In[4]:


st = 'Print only the words that start with s in this sentence'
for item in st.split() :
    if item.startswith("s"):
        print(item)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[1]:


for item in range(0,11) : 
    if item %2==0 : 
        print(item," is even")


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[5]:


for item in range(1,51) :
    if item %3==0 :
       print(item)


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[ ]:


st = 'Print every word in this sentence that has an even number of letters'


# In[ ]:


st = "Print every word in this sentence that has an even number of letters"
if len(st)%2==0 :
    print("Even")
else:
    print("Odd")


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[ ]:


for item in range(1,101) :
    if item %3==0 :
        if item%5==0 :
            print("fizz bazz")
        else :
            print("fizz")

    elif item %5==0 :
        if item%3==0 :
            print("fizz bazz")
        else :
            print("buzz")


    else:
        print(item)


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[ ]:


mylist=[]
st = 'Create a list of the first letters of every word in this string'
for i in st.split():
    mylist.append(i[0])
print(mylist)


# ### Great Job!


# In[ ]:




