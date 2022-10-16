def convert(n): #Ввод критериев в матрицу n*n
    try:
        n = int(n)
    except Exception:
        return -1
    return n
def inputTable(table, n):
    #Ввод отношений для верхней половины матрицы
    for i in range(n):
        for j in range(n):
            if (i == j):
                table[i][j] = 1 #Элементы главной диагонали равны единице
            if (i < j):
                while table[i][j] == 0: #Для выхода из цикла ввода элемента ожидается верный ввод
                    temp = input("Введите отношение критерия {0} к критерию {1} ".format(i+1, j+1))
                    temp = convert(temp)
                    if (temp == -1) or (1 <= temp <= 9) == False: #Проверка на соответствие условиям
                        print('Отношение должно быть целым числом от 1 до 9')
                    else:
                        table[i][j] = temp
    #Отражение матрицы по главной диагонали и возведение её элементов в -1 степень
    for i in range(n):
        for j in range(n):
            if (i > j):
                table[i][j] = 1/table[j][i]
    return table
#Вывод матрицы попарных сравнений
def outputTablePrecise(table, n):
    for i in range(n):
        for j in range(n):
            print("{0:.4f}".format(table[i][j]), end=" ")
        print()
#Cуммирование всех элементов матрицы
def tableSum(table, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += table[i][j]
    return sum
#Расчёт весовых коэффициентов
def count(table,n,sum):
    columnSum = 0
    arrayWQ  = list()
    #расчёт суммы отношений для каждого критерия
    for i in range(n):
        for j in range(n):
            columnSum += table[j][i]
        arrayWQ.append(columnSum/sum)
    return arrayWQ

#Основная чать программы
n = 0
#Ввод количества критериев
while n == 0: #Цикл будет запрашивать ввод, пока количество не будет положительным целым числом
    n = input("Введите количество критериев: ")
    n = convert(n)
    if (n == -1) or (n < 1):
        print("Количество критериев должно быть положительным целым числом")
        n = 0
a = [[0] * n for i in range(n)] # Создание массива n*n
a = inputTable(a,n)
print("\nМатрица попарного сравнения: ")
outputTablePrecise(a,n)
a_sum = tableSum(a,n)
WQ = count(a,n,a_sum) #Создание массива, хранящего весовые коэффициенты
WQ.reverse()
print("Весовые коэффициенты:", end=" ")
for elem in WQ:
    print("{0:.2f}".format(elem), end=" ") #Форматирование вывода для соответствия условиям задачи