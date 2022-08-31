from ctypes import Union
from operator import le


n1=int(input())
n2=int(input())
a=[]
b=[]
for i in range(n1):
    a.append(int(input()))
for i in range(n2):
    b.append(int(input()))
print(a,b)
c=list(set(a)|set(b))
print(c)
c=list(sorted(c))
print(c)
if(len(c)%2!=0):
    ans=c[int(len(c)/2)]
else:
    ans=(c[int(len(c)/2)]+c[int(len(c)/2)-1])/2
    print("run")
    print(c[int(len(c)/2)])
    print(c[int(len(c)/2)-1])
print("{:.2f}".format(ans))