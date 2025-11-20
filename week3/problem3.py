s = input("nhập vào một từ: ")

s = s.lower()
l = s.split()

lm = []
for i in l:
    if(lm.count(i) == 0):
        lm.append(i)

s1 = lm[0]
ct = l.count(s1)
for i in lm:
    if(l.count(i) > ct):
        s1 = i
        ct = l.count(i)
print("từ xuất hiện nhiều nhất là: ", s1)
print("số lần xất hiện là: ", ct)

for i in range(len(lm)):
    for j in range(i, len(lm)):
        if(len(lm[i]) < len(lm[j])):
            ts = lm[i]
            lm[i] = lm[j]
            lm[j] = ts
print("danh sách các từ sắp xếp giảm dần là: ", lm) 
