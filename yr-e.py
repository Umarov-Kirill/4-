while True:
    a = input("Введите а: ")
    if (isinstance(int(a), int)):
        a = int(a)
        print("ok")
    else:
        a = int(input("Введите ЧИСЛО, равное а!"))

    b = input("Введите b: ")
    if (isinstance(int(b), int)):
        b = int(b)
        print("ok")
    else:
        b = int(input("Введите ЧИСЛО, равное b!"))
    c = input("Введите c: ")
    if (isinstance(int(c), int)):
        c = int(c)
        print("ok")
    else:
        c = int(input("Введите ЧИСЛО, равное c!"))
    x1 = 0
    x2 = 0
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + d**0.5)/(2 * a)
        x2 = (-b - d**0.5)/(2 * a)
    elif d==0:
        x1 = -b/(2 * a)
        x2 = -b/(2 * a)
    else:
        x1 = 0
        x2 = 0
    print(x1)
    print(x2)
