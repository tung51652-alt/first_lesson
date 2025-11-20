ds = input()

ten = set()
dsl = []
for i in range(len(ds)):
    name = ""
    diem = ""
    j = i
    while(ds[j] != ":"):
        name.join(ds[j])

    j += 1
    while(ds[j] != "," or j < len(ds)):
        diem.join(ds[j])

    tp = (name, int(diem))
    dsl.append(tp)
    ten.add(name)
    i = j

print(dsl)

