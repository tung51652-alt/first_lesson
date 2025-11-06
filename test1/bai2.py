s = input()

d = {}
for i in s:
    a = i.lower()
    if(not(a in d)):
        d[a] = 1
    else:
        d[a] += 1
print(d)
