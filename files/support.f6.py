f=open("files/file.txt","r+")
lst=f.read()
lst=lst.replace("guli","gulijon")
f.seek(0)
f.write(lst)
f.close