str1=input("enter your string")
str2="  " 
c="?!,.@#/()[]{}|"
for i in str1:
    if i not in c:
        str2=str2+i.lower()
print(str2)