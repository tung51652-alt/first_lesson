item = []

def create_item(*infor):
    item.append({"name": infor[0], "qty": infor[1], "price": infor[2]})

def total():
    return sum(i["qty"] * i["price"] for i in item)

create_item("pen", 2, 5.0)
create_item("notebook", 1, 15.0)

print("Customer: Nguyen van A")
print("-----------------------")
print(f"{'Product':<10}{'Qty':>5}{'Price':>10}{'Subtotal':>12}")
for i in item:
    print(f"{i['name']:<10}{i['qty']:>5}{i['price']:>10.2f}{i['qty']*i['price']:>12.2f}")
print("-----------------------")
print(f"{'Total:':<25}{total():>12.2f}")