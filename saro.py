'''a="saravanan"
print(a.center(30))
b="am saravanan"
print(b.capitalize())
print(a[::-1])
print(b[::-2])

#duplicate
s="saravanan"
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)

# vowels

a="saravanan kumar"
c=0
for i in s:
    if i in "aeiou":
        c+=1
print("no of vowles:",c)




# TASK 1


string=input("enter the name:")
temp=""
for i in string:
    temp=i+temp
if temp==string:
     print("true")
else:
     print("false")

# TASK 2

string=input("enter the name:")
vowel_count=0
for i in string:
    if  i in "aeiouAEIOU":
        vowel_count+=1
print("no vowels ;",vowel_count)

# TASK 3

a=input("enter the name :")
reverse=""
for i in a:
    reverse=i+reverse
print(reverse)

# TASK 4

a=input("enter the name :")
lower=0
upper=0
for i in a:
    if i in "qwertyuioplkjhgfdsazxcvbnm":
        lower+=1
    elif i in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        upper+=1
print("upper :",upper)
print("lower :",lower)


# TASK 5

s=input("enter the name :")
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)'''

# TASK 12
s=input("enter the name :")
a=s.title()
print(a)







           



    


