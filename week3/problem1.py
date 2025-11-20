ds = set(map(int, input("nhap so vao danh sach: ").split()))

print("loại bỏ phần tử trùng: ", ds)
l = []


for i in ds:
    if(i % 2 == 0):
        l.append(i**2)
    else:
        l.append(i**3)

print("mảng theo yêu cầu là: ", l)

dsl = list(ds)
c = []
for i in range(len(dsl)):
    if(i % 2 == 0): 
        c.append(dsl[i])

print("trung binh index chan: ", sum(c)/len(c))

for i in range(len(dsl)):
    for j in range(i, len(dsl)):
        if(abs(dsl[i]) > abs(dsl[j])):
            tmp = dsl[i]
            dsl[i] = dsl[j]
            dsl[j] = tmp
print("sắp xếp theo abs là: ", dsl)