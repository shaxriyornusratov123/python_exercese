f=open("files/file.txt","r")
a=f.read().split()
k=a[0]
for i in a:
    if len(i)>len(k):
        k=i
print(k)

f.close()

