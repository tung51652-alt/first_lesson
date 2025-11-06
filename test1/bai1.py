ds = input()

l = ds.split(", ")
t = tuple(l)
print("kho hang (tuple): ", t)
print("tổng số loại hàng: ", len(l))
l1 = ["Phone", "Laptop", "Smartwatch"]
bc = []
kbc = {w for w in l if(l1.count(w) == 0)}
for i in l:
    if(l1.count(i) != 0 and bc.count(i) == 0): 
        bc.append(i)
        
print("san pham ban chay la: ", bc)
print("san pham khong ban chay la: ", kbc  )


