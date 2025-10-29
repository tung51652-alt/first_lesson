x = int(input("nhap vao x: "))
n = int(input("nhap n: "))

res1 = 1 
res2 = 0

i = 1
gt = 1
while(i <= n):
    res1 += (x**i)/gt
    res2 += 1/gt
    i += 1
    gt *= i

print("e^x = ", res1)
print("S = ", res2)


