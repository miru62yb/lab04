rejected_count = 0
while True:
    num = int(input("Введите число: "))
    if num > 0:
        print("Квадрат:", num ** 2)
        print("Отклонённых попыток:", rejected_count)
        break
    rejected_count += 1
