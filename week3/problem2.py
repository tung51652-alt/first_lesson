s = input("nhap vao mot chuoi: ")
s = s.lower()


nm = "ueoai"
c = 0
for i in s:
    if(nm.find(i) != -1): c += 1

print("so luong nguyen am: ", c)
print("so luong phu am: ", len(s) - c)

temp = s[::-1]
if(temp == s):
    print("Palindrome: True")
else:
    print("Palindrome: False")


s1 = "".join(i for i in s if i.isalpha() or i.isspace())

print("chuẩn hóa: ", s1)
l = s1.split()
ld = [w[::-1] for w in l]
print("đâỏ từ: ", ld)
