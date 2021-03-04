#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check (x,y) :
    if(x%2==0+y%2==0):
        if(x<y):
            return x
        else:
            return y
    else:
        if (x < y):
            return y
        else:
            return x

num_1=int(input("Please Enter number 1 : "))
num_2=int(input("Please Enter number 2 : "))
print(check(num_1,num_2))


def check (x,y) :

    for i in range(1) :
        if(x[i]==y[i]):
            return 1



str_1=(input("Please Enter word 1 : "))
str_2=(input("Please Enter word 2 : "))
if(check(str_1,str_2)==1):
    print("true")
else:
    print("False")


def check (x,y) :
    if((x+y)==20):
        return 1



num_1=int(input("Please Enter integer number 1 : "))
num_2=int(input("Please Enter integer number 2 : "))

if(check(num_1,num_2)==1):
    print("true")
else:
    print("False")



def check (x) :

    for i in range(len(x)):
        if (i==3):
            print(x[i].capitalize())
        elif(i==0):
            print(x[i].capitalize())
        else:
            print(x[i])



str_1=(input("Please Enter word 1 : "))
check(str_1)



def check (x) :

    print(x[::-1])
   


str_1=(input("Please Enter word 1 : "))
check(str_1)



def almost_there(n):
    pass


almost_there(104)


almost_there(150)

almost_there(209)

def has(nums):
    for x in range(len(nums)-1):
        if (nums[x] == 3) and (nums[x+1] == 3):
            return 1


nums1=[1,3,3,4]
if(has(nums1)==1):
    print("true")


def paper_doll(text):
    pass

paper_doll('Hello')


paper_doll('Mississippi')



def blackjack(a,b,c):
    pass

blackjack(5,6,7)

blackjack(9,9,9)


blackjack(9,9,11)



def summer_69(arr):
    pass

summer_69([1, 3, 5])


summer_69([4, 5, 6, 7, 8, 9])


summer_69([2, 1, 6, 9, 11])
([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    pass


spy_game([1,2,4,0,0,7,5])

spy_game([1,0,2,4,0,5,7])


spy_game([1,7,2,0,4,5,0])



def count_primes(num):
    pass
                


count_primes(100)



def print_big(letter):
    pass



print_big('a')


# In[ ]:





# In[ ]:





# In[ ]:




