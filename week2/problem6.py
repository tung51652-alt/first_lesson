
food = 0
cost = 0
while True:
   
    f = input()
    
    if(f == 'x' or f == 'X'):
        break
    elif(f == "pass"):
        f = input()
        continue
    elif(f == "skip"):
        continue

    sf = f.split()
    n = int(sf[1])
    food += 1
    cost += n 


print("Số món: ", food)
print(f"Tổng tiền trước giảm giá:{cost} VND ")

discout = int(cost*10/100) if(cost > 200000) else 0
print(f"Giảm giá 10% (nếu đơn hàng trên 200.000VND): {discout} ")
print(f"Tổng tiền sau giảm giá: {cost - discout}")
