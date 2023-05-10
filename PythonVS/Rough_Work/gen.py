def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,(a+b)

f1 = fibonacci()
while True:
    a = int(input("Enter number: "))
    
    if a == 0:
        break
    else:
        count = 0
        for i in f1:
            if count == a:
                break
            else:
                count += 1
                print(i)


