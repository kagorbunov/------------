import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(lecture, laboratoryWork, cheerfulness, friend):
    x = np.array([lecture, laboratoryWork, cheerfulness, friend])
    w11 = [0, 1, 0, 0]
    w12 = [0, 0, 0.4, 0.4]
    w13 = [0.4, 0, 0.4, 0]
    weight1 = np.array([w11, w12, w13])
    weight2 = np.array([1,1,1]) # вектор 1х2
    sum_hidden = np.dot(weight1, x) # вычисляем сумму на входахнейронов скрытого слоя
    print("Значения сумм на нейронах скрытого слоя: "+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходах нейронов скрытого слоя:"+str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Выходное значение НС: "+str(y))

    return y

lecture = int(input("Введите [1/0], если не скучная лекция: "))
laboratoryWork = int(input("Введите [1/0], если важная лабораторная работа: "))
cheerfulness = int(input("Введите [1/0], если студент бодрый с утра: "))
friend = int(input("Введите [1/0], если на пару пойдет его друг: "))
res = go(lecture, laboratoryWork, cheerfulness, friend)
if res == 1:
    print("Сегодня день начинается с первой пары!")
else:
    print("Посплю еще пол часика...")


