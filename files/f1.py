#2# f=open("files/file.txt","r")
# print(f.read())
# f.close




#5#################################
f=open("files/file.txt","r")      
a=f.read().split()                
print(len(a))                            



#6 
f=open("files/file.txt","r")
a=len(f.read())
print(a)
f.close()


# #7
# f=open("files/file.txt","r")
# f.read()
# f=open("files/file1.txt","r")

#9
try:
    open("files/hello.txt","x")
except FileExistsError:
    print("fiel exists,continue...")
f=open("files/hello.txt","r")

text=f.read()
print(text)
print("eshmat" in text)
f.close()

#10
for i in range(5):
    open (f)