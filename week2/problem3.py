
n = int(input("nhap so luong nguoi: "))
people = []
grade = []

for i in range(n):
    name = input(f"nhập tên người {i+ 1}: ")
    g1 = int(input("nhập điểm 1: "))
    g2 = int(input("nhập điểm 2: "))
    people.append(name)
    grade.append(g1 + g2)

z1 = zip(people,grade)
i = 1

for name,g in z1:
    d = ""
    if(g >= 200):
        d = "Xuất sắc"
    elif(g >= 150):
        d = "Giỏi"
    elif(g >= 100):
        d = "Khá"
    else:
        d = "Yếu"
    
    print(f"{i} {name} {g} {d} ")
    i+=1

