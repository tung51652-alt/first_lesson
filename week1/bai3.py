print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Truong CNTT  - “10 diem”")

s = "CLB Tin Hoc HIT truc thuoc Truong CNTT"

hoa = []
thuong = []
for x in s:
    if(x.isupper()):
        hoa.append(x)
    else:
        thuong.append(x)

print(hoa)
print(thuong)

if(s.find("CNTT")):
    print("YES")
else:
    print("NO")

print(s.swapcase())