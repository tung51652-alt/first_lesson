email = input("nhập email để kiểm tra: ")

d = email.find('@')
if( d != -1 and d > 0):
    x = email.find('.',d)
    
    if( x != -1 and x - d > 1 ):
        print("Valid")
    else:
        print("Invalid")

    

else:
    print("Invalid")