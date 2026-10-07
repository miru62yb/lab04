n = int(input())
first = int(input())
total = first
positive_count = 1 if first > 0 else 0
max_val = first
for _ in range(n - 1):
    num = int(input())
    total += num
    if num > 0:
        positive_count += 1
    if num > max_val:
        max_val = num
print("Сумма:", total)
print("Количество положительных:", positive_count)
print("Максимум:", max_val)