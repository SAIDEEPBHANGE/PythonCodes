# level 0=data type and type casting
print("hello world")
print("hello\\ world")
print("\"hello world\"")
print("\'hello world\'")
var1="hello world"
var2=4
var3=36.7
var4="i am saideep"
var5="100"
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(var1+var4+var5)
print(var2+int(var5))
print(10*(var1+"\n"))
print(100*var2+int(var5))
print(10*(str(var2+int(var5))+"\n"))
# ------------------------------------
# level 1= input and output
print("enter a number")
var6=input()
print(var6," ",type(var6))
print("enter a number")
var7=int(input())
print(var7," ",type(var7))
# ------------------------------------
# level 2=string slicing
var8="SAIDEEP ARVIND BHANGE"
var9="saideep"
print("string var8 is \"",var8,"\"")
print("string var9 is \"",var9,"\"")
print("var8[0]: ",var8[0])
print("var8[8]: ",var8[8])
print("var8[15]: ",var8[15])
print("var8[0:7]: ",var8[0:7])
print("var8[0:21:2]: ",var8[0:21:2])
print("var8[::]: ",var8[::])
# print("var8[0:-7]: ",var8[-1:-3]) problem here
print("var8.isalnum() check spaces in string: ",var8.isalnum())
print("var9.isalnum() check spaces in string: ",var9.isalnum())
print("var8.isalpha() check spaces in string: ",var8.isalpha())
print("var9.isalpha() check spaces in string: ",var9.isalpha())
print("var8.endswith(\"NGE\"): ",var8.endswith("NGE"))
print("var9.endswith(\"eep\"): ",var9.endswith("eep"))
print("var8.count(\"A\"): ",var8.count("A"))
print("var9.capitalize(): ",var9.capitalize())
print("var8.find(\"ARV\"): ",var8.find("ARV"))
print("var8.lower(): ",var8.lower())
print("var9.upper(): ",var9.upper())
print("var8.replace(\"SAIDEEP\",\"KIRTI\"): ",var8.replace("SAIDEEP","KIRTI"))
# ------------------------------------
# level 3=list=mutable
var10=["SAIDEEP","Arvind","bhange",56,5.78,True,False]
print("var10: ",var10,"\ttype(var10): ",type(var10),"\tlen(var10): ",len(var10))
var11=[12,265,56145,46856,12,4,56,125,33,658,0,556,545,628855]
print("var11: ",var11,"\ttype(var11): ",type(var11),"\tlen(var11): ",len(var11))
# var11.sort()
# print("var11.sort(): ",var11)
# var11.reverse()
# print("var11.reverse()",var11)
print("var11[:5]: ",var11[:5])
print("var11[5:]: ",var11[5:])
print("var11[::3]: ",var11[::3])
print("max(var11): ",max(var11))
print("min(var11): ",min(var11))
var11.append(1)
print("var11.append(1): ",var11)
var11.insert(1,45644585898)
print("var11.insert(1,45644585898): ",var11)
var11.remove(0)
print("var11.remove(0)",var11)
var11.pop()
print("var11.pop()",var11)
# ------------------------------------
# level 3=tuple=inmutable
var12=(1,2,3,4,6,8,44,5)
print("var12: ",var12,"\ttype(var12): ",type(var12),"\tlen(var12): ",len(var12))
# ------------------------------------
# level 4=dictionary
var13={"me":"SAIDEEP","father":"ARVIND","mother":"KIRTI","sister":"SHRADDHA","family":{"Me":"saideep","Father":"arvind","Mother":"kirti","Sister":"Shraddha"}}
print("var13: ",var13,"\ttype(var13): ",type(var13),"\tlen(var13): ",len(var13))
print("var13[\"me\"]: ",var13["me"])
print("var13[\"family\"]: ",var13["family"])
print("var13[\"family\"][\"Me\"]: ",var13["family"]["Me"])
var13["grandmother"]="rekha aaji"
del var13["family"]
print("var13: ",var13,"\ttype(var13): ",type(var13),"\tlen(var13): ",len(var13))
var14=var13.copy()
print("var14=var13.copy(): ",var14)
print("var14: ",var14,"\ttype(var14): ",type(var14),"\tlen(var14): ",len(var14))
print("var13.keys(): ",var13.keys(),"\nvar14.keys(): ",var14.keys())
print("var13.items(): ",var13.items(),"\nvar14.items(): ",var14.items())
# ------------------------------------
# level 5=set
var15=set([2,4])
var15.add(1)
var15.add(100)
var16=set([1,4,5,88,98,125])
print("var15: ",var15,"\ttype(var15): ",type(var15),"\tlen(var15): ",len(var15))
print("var16: ",var16,"\ttype(var16): ",type(var16),"\tlen(var16): ",len(var16))
print("var15.union(var16): ",var15.union(var16))
print("var15.intersection(var16): ",var15.intersection(var16))
print("var15.isdisjoint(var16): ",var15.isdisjoint(var16))
# ------------------------------------
# level 6=ifelse
var17=int(input())
var18=int(input())
if var17>var18:
    print(var17," is greater")
elif var18==var17:
    print(var17," and ",var18," are equal")
else:
    print(var18," is greater")
var19=[5,7,3]
if 5 in var19:
    print("5 in the list : ",var19)
else:
    print("5 in not list")
if 15 not in var19:
    print("15 is not in list")
else:
    print("15 is in list")
var20=int(input("enter age: "))
if var20 == 18:
    print("we think about it")
elif var20>18:
    print("you can drive")
else:
    print("no you cannot drive")
# ------------------------------------
# level 7=for loop
var21=["SAIDEEP","Arvind","bhange",56,5.78,True,False]
for i in var21:
    print("i: ",i," type(i): ",type(i))
var22=[["me","SAIDEEP"],["father","ARVIND"],["mother","KIRTI"],["sister","SHRADDHA"]]
for i,j in var22:
    print("my",i," is ",j)
var23=dict(var22)
for i,j in var23.items():
    print("my",i," is ",j)
# ------------------------------------
# level 8=while loop
var24=0
while(var24<45):
    print(var24)
    var24+=1
# ------------------------------------
# level 9=break and countinue
var25=1
while(True):
    if var25%2==0:
        var25+=1
        continue
    if var25==45:
        break
    var25+=1
    print(var25,end=" ")
# ------------------------------------
# level 10=functions
var26=int(input("\nvar26: "))
var27=int(input("var27: "))
var28=sum((var26,var27))
print("var28: ",var28," type(var28): ",type(var28))
def fun_01():
    '''saideep printing'''
    print("saideep")
def fun_avg(a,b):
    '''avgerage printing'''
    return int((a+b)/2)
fun_01()
print("fun_avg(10,19): ",fun_avg(10,19)," type(fun_avg(10,19)): ",type(fun_avg(10,19)))
print(fun_01.__doc__,fun_avg.__doc__)
# ------------------------------------
# level 11=try and catch method
try:
    var29=int(input("var29: "))
    var30=int(input("var30: "))
    print("sum of var29 and var30 is: ", var29+var30)
except Exception as e:
    print(e)
print("this is important message")
# ------------------------------------
# level 12=anonymous function
myadd=lambda var31,var32: var31+var32;
mysub=lambda var31,var32: var31-var32;
print("addition : ",myadd(15,20))
print("substraction : ",mysub(15,20))
# ------------------------------------
# level 13=list comprehension
var33=[i**2 for i in range(10)]
print("var33: ",var33," type(var33): ",type(var33))
var34=[i*2 for i in var33]
print("var34: ",var34," type(var34): ",type(var34))
var35=["SAIDEEP","ARVIND","BHANGE"]
print("var35: ",var35," type(var35): ",type(var35))
var36=[i[0] for i in var35]
print("var36: ",var36," type(var36): ",type(var36))
print(i[0] for i in var35)
