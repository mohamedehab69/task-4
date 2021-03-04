#!/usr/bin/env python
# coding: utf-8

# In[2]:



st = 'Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
for item in st.split() :
    if item.startswith("s"):
        print(item)



for item in range(0,11) : 
    if item %2==0 : 
        print(item," is even")

for item in range(1,51) :
    if item %3==0 :
       print(item)



st = 'Print every word in this sentence that has an even number of letters'




st = "Print every word in this sentence that has an even number of letters"
if len(st)%2==0 :
    print("Even")
else:
    print("Odd")



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


st = 'Create a list of the first letters of every word in this string'


mylist=[]
st = 'Create a list of the first letters of every word in this string'
for i in st.split():
    mylist.append(i[0])
print(mylist)


# In[ ]:




