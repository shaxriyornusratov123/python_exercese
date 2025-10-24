import os
try:
    
    os.chdir("files")
    print(os.getcwd())
    old_sub=input("old_sub: ")
    new_sub=input("new_sub: ")
    os.rename(old_sub,new_sub)
except FileExistsError :
    print("boshqa nomli file yozing ")
