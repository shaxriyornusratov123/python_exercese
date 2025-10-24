n=list(map(int,input().split()))
f=open("even_nums.txt","w") 
for i in n:
    if i%2==0:
        f.write(str(i))

f.close()
