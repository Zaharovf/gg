#2
a = int(input("Введите 5ти значное число:"))
if a < 10000 or a > 99999:
    print("не 5 значное")
else:
    a1 = a // 10000
    a2 = a % 10
    print(a1, a2)