n=int(input("enter the size of list:"))
l=[]
for i in range(0,n-1):
    ele=input("enter the element")
    l.append(ele)
    print(f"{ele}inserted succesully")
print(l)