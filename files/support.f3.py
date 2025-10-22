f=open("files/hello.txt","r")
a=f.readlines()
f.close()
f=open("files/even.num.txt","a")
for i in a:
    i=i[:-1]
    f.write(i[::-1]+"\n")
f.close()
