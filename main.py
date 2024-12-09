# module_2_4

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

for number in numbers:
    # Переменная для определения простоты числа
    is_prime = True

    if number == 1:
        continue  # Число 1 не простое и не составное, пропускаем его

    # Проверяем делимость числа от 2 до самого числа (исключая само число)
    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
            break  # Если нашли хотя бы один делитель то прекращаем проверку

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим результаты
print("Primes:", primes)
print("Not Primes:", not_primes)
