#!/usr/bin/env python
# coding: utf-8

# In[1]:


file=open("Ass4.text",'w')
for item in range(0,5) :
   file.write("Hello World\n")
file.write("\n")
file.close()

print("\n")
file=open("Ass4.text",'r+')
for item in range(0,5) :
   if item==2 :
      pr = file.readline()
      file.write(pr.capitalize())
   else :
      pr = file.readline()
      file.write(pr.upper())
file.close()


file=open("Ass4.text",'r')
print(file.readlines(4))
file.close()


file=open("Ass4.text",'a')
file.write("\nI love you")
file.close()


# In[ ]:




