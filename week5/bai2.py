

def find_by_id(data, id):
    for i in data:
        if(i["id"] == id):
            print("id: ", i["id"], "name: ", i["name"], "score :", i["score"])

def filter_by_score(data, min_score):
    res = []
    for i in data:
        if(i["score"] >= min_score):
            res.append(i)
    print(res)

def sort_by_score(data, reverse = False):
    data.sort(key = lambda i: i["score"], reverse = reverse)
    res = data.copy()
    return res

def add_student(data, new):
    data.append(new)

def remove_student(data, id):
    for i in data:
        if(i["id"] == id):
            data.remove(i)

def statistics(data):
    mean = 0
    highest = data[0]
    lowest = data[0]
    for i in data:
        mean += i["score"]
        if(i["score"] > highest["score"]): highest = i
        if(i["score"] < lowest["score"]): lowest = i

    print("mean = ", mean/len(data))
    print("highest = ", highest)
    print("lowest = ", lowest)

students = [

    {"id": 1, "name": "An", "score": 8.5},

    {"id": 2, "name": "Bình", "score": 7.2},

    {"id": 3, "name": "Chi", "score": 9.0}

]

print(find_by_id(students, 2))
filter_by_score(students, 8.0)
print(sort_by_score(students))
new_student = {"id": 4, "name": "Dung", "score": 6.8}
add_student(students, new_student)
print(students)
remove_student(students, 1)
print(students)
statistics(students)