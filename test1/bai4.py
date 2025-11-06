n = list(map(int, input().split()))

s = 0
e = 0
c = 0

i = 0
while i < len(n):
    
    j = i + 1
    while(j < len(n) and n[i] != n[j]):
        j += 1
    
    ts = i
    te = j - 1
    if( te - ts + 1 > c):
        s = ts
        e = te
        c = e - s + 1
    i = j - 1
    i += 1


tp = (n[s:e+1])
print("Đoạn con dài nhất: ", tp)
print("Độ dài: ", c)


    