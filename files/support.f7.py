f=open("files/file.txt","r")
word=f.readlines()
f.close()
special=input("words")
f=open("files/file2.txt","a")
for i in word:
    if special in i :
        f.write(i)
f.close()
