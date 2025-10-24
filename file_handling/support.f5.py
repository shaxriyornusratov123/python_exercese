f=open("files/file.txt","r")
a=f.read().split()
f.close()
d={}
for w in a:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
print(d)
    