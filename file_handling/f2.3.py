with open("files/file.txt","r+") as f , open ("files/file3.txt","w") as f2:
    res=f.read()
    f2.write(res)
