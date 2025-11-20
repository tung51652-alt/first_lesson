
def remove_punctuation(s):
    res = ""
    for i in s:
        if(i.isalnum() or i == " "):
          res += i
    return res

def remove_stopwords(s):
    stopwords = ["is", "a", "this"]
    arr = s.split(" ")
    res = ""
    for i in arr:
        if(i not in stopwords):
                res += i + " "

    return res

def count_words(s):
    arr = s.split(" ")
    ds = dict()
    for i in arr:
        if i in ds:
            ds[i] += 1
        else:
            ds[i] = 1
    print(ds)


s = input()

print("loai bo ki tu")
s = remove_punctuation(s)
print(s)
print("dua ve in thuong")
a = lambda s : s.lower()
s = a(s)
print(s)
print("loai bo chu dung")
s = remove_stopwords(s)
print(s)
count_words(s)