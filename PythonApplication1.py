
import math


while(True):
    try:
        kat1 = int(input("Введите длинну первого катета "))
    
        kat2 = int(input("Введите длинну второго катета "))
    except ValueError:
        print("Значение не должно быть строкой")
        continue
    if kat1 == 0 or kat2 == 0:
        break

    print("Длинна первого катета равна " + str(kat1))
    print("Длинна второго катета равна " + str(kat2))

    gip = round(math.sqrt(kat1**2+kat2**2),2)
    P = round(int(kat1)+int(kat2)+int(gip),2)
    S = round((int(kat1)*int(kat2))/2,2)

    print("Длинна гипотенузы равна " + str(gip))
    print("Периметр треугольника составляет "+ str(P))
    print("Площадь треугольника составляет "+ str(S))