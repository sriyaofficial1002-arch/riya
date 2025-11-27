l=[1,2,3,4]
print(l*2)

l=[1,2,1]
r=[ ]
for i in range(0,2):
    for j in range(0,len(l)):
        r.append(l[j])
print(r)