import os
sub="files/practic_dir"
os.chdir(sub)
print(os.getcwd())
with open("hi.txt","r") as f:
    f.read()

print(os.path.exists("hi.txt"))