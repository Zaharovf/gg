a = int(input("Введите 4х значное число"))
if a < 1000 or a > 9999:
    print("не 4х значное")
else:
    a4 = a % 10 
    a3 = a // 10 % 10 
    a2 = a // 100 % 10 
    a1 = a // 100 // 10 
    C = a1 + a2 + a3 + a4 
    Z = a1 * a2 * a3 * a4 
    print(C, Z)
