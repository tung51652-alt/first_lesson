code = input()

d = {}
i = 0
while i < len(code):
    if(code[i].isdigit()):
        j = i + 2
        while code[j] != ']':
            j += 1

        d[code[i + 2 : j]] = int(code[i])
        i = j
    elif('a' <= code[i] and code[i] <= 'z'):
        j = i
        while(j < len(code) and  (code[j].isalpha())):
            j += 1

        #print(i, " ", j)
        d[code[i:j]] = 1
        i = j - 1

    i += 1


s = ""
for k,v in d.items():
    s += k*v
print(s)
        