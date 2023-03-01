import numpy

USE_STDLIB = True
USE_RANDOM = False


# Функция проверки ввода
def myp_input(x):
    try:
        x = int(input())
        return x
    except ValueError:
        print("Введены неверные данные")
        exit()


def myp_matrix_output(v):
    # Открываем файл и присваиваем его переменной
    with open("MypoutputLab2.txt", "a+") as f:
        for row in v:
            for col in row:
                # Записываем строку в файл
                f.write(f"{col} ")
            f.write("\n")
        f.write("\n")


def myp_list_output(v):
    # Открываем файл и присваиваем его переменной
    with open("MypoutputLab2.txt", "a+") as f:
        for row in v:
            # Записываем строку в файл
            f.write(f"{row} ")
        f.write("\n\n")


if __name__ == '__main__':
    N = int()
    M = int()
    my_file = open("MypoutputLab2.txt", "w")

    # Ввод
    print("Введите размер матрицы X * Y")
    N = myp_input(N)
    M = myp_input(M)

    # заполнение массива рандомными числами
    matrix = numpy.random.uniform(0, 5, (N, M))

    # вывод матрицы
    #myp_matrix_output(matrix)

    # создание массива максимумов по строкам
    maximy = numpy.max(matrix, axis=1)

    #myp_list_output(maximy)

    # обработка матрицы
    for i in range(N):
        for j in range(M):
            matrix[i][j] /= maximy[i]

    # вывод матрицы после обработки
    myp_matrix_output(matrix)

