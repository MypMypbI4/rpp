import random

USE_STDLIB = True
USE_RANDOM = True


# Функция для замены sum()
def my_sum(x):
    summ = 0
    for val in x:
        summ += val

    return summ


# Функция для замены len()
def my_len(x):
    ai = 0
    for val in x:
        ai += 1

    return ai


if __name__ == '__main__':
    if USE_RANDOM:
        A = []
        # Генерация и вывод 10 чисел
        arr = [random.randint(1, 100) for _ in range(10)]
        print(*arr)
    else:
        A = []
        # Получение чисел в виде строки и преобразование в список
        # Также здесь есть проверка на правильность ввода
        try:
            arr = list(map(int, input("Введите числа: ").split()))
        except ValueError:
            print("Введены неверные данные.")
            exit()

    if USE_STDLIB:
        # Используя стд либу
        for i in range(len(arr)):
            if arr[i] > sum(arr)/len(arr) and arr[i] % 2 == 0:
                A.append(arr[i])
        for i in range(len(A)):
            arr.remove(A[i])
    else:
        # НЕ используя стд либу
        for i in range(my_len(arr)):
            if arr[i] > my_sum(arr)/my_len(arr) and arr[i] % 2 == 0:
                A.append(arr[i])
        for i in range(my_len(A)):
            arr.remove(A[i])

    print(*arr)
