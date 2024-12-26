from random import randint

numbers = []
for i in range(1, 100):
    numbers.append(randint(0, 100))

print(numbers)

find = randint(0, 100)
print("Ищем:", find)

def search_numbers(numbers, find):
    pos = []
    for i, num in enumerate(numbers):
        if num == find:
            pos.append(i)
    return pos

pos = search_numbers(numbers, find)

if not pos:
    print("Элемент не найден")
else:
    print(f"Найдено на позициях: {pos}")
