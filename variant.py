n = int(input("Введите n: "))
count = 0
total_sum = 0
for _ in range(n):
    num = int(input("Введите число: "))
    if num % 2 == 0:
        count += 1
        total_sum += num
print("Количество:", count)
print("Сумма:", total_sum)
