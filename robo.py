n = int(input())
cnt=0
while n>0:
    raqam=n%10
    cnt+=raqam
    n//=10
print(cnt)
