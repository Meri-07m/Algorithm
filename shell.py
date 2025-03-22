l=[14,1,22,3,36,9,63,128,5,2]
n=len(l)
t=n//2
while t>0:
    for x in range(t,n):
           temp=l[x]
          J=x
          while J>= t and l[J-t]> temp:
                   l[J]=l[J-t]
                   J-=t
          l[J]=temp
    t//=2
print(l)
