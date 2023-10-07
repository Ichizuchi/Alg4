import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import timeit

def findmin():
    min = randmax
    for i in a:
        if min > i:
            min = i
    return min
def findmax():
    max = 0
    for i in a:
        if max < i:
            max = i
    return max
def create_graph(b, c, aur, bur, namegraph):
    plt.scatter(b, c, s=5)
    y_line = aur * np.array(b) + bur
    plt.plot(b, y_line, color='red')
    plt.title(namegraph)
    plt.xlabel("Размер массива")
    plt.ylabel("Время работы функции")
    correlation_coefficient = np.corrcoef(c, b)[0, 1]
    return correlation_coefficient


correlation_v = []
# Цикл минимума и максимума
for namegraph in ["Минимум", "Максимум"]:
    x = [i for i in range(10, 10001, 10)]
    time = []
    x2 = []
    xtime = []
    randmax = 1000000
    if namegraph == "Минимум":
        for i in x:
            a = [rnd.randint(0, randmax) for j in range(i)]
            time.append((timeit.timeit(lambda: findmin(), number=50))/50)
    else:
        for i in x:
            a = [rnd.randint(0, randmax) for j in range(i)]
            time.append((timeit.timeit(lambda: findmax(), number=50))/50)

    sx = sum(x)
    stime = sum(time)
    sx2 = sum(i**2 for i in x)
    sxtime = sum(i*j for i, j in zip(x, time))
    n = len(x)
    k = sx2/sx
    bur = (sxtime - k*stime)/(sx-k*n)
    aur = (stime - bur*n)/sx
    plt.figure(namegraph)
    plt.subplots_adjust(left=0.2)

    correlation_v.append(create_graph(x, time, aur, bur, namegraph))

print(" \n Коэффициент корреляции в первом случае =",
      correlation_v[0], "\n во втором случае =", correlation_v[1])

# Показ графика
plt.show()