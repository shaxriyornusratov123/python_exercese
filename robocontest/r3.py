
siljish = int(input())
matn =input()
natija = ""

for harf in matn:
    if harf.isalpha():
        start = ord('A') if harf.isupper() else ord('a')
        natija += chr((ord(harf) - start + siljish) % 26 + start)
    else:
        natija += harf

print(natija)

