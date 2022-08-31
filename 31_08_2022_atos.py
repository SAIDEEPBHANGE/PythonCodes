def code(a,pos):
    res=""
    for i in range(0,(len(a)),2):
        res+=(a[i]*(int(a[i+1])))
    if pos<=len(res):
        return a[pos-1]
    else:
        return str(-1)
print(code("a1b1c3",7))