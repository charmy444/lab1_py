def is_num(x):
    #Проверка на то, является ли символ числом
    try:
        float(x)
    except:
        return False
    return True


def both_is_int(x, y):
    #Проверка на то, что оба числа являются целочисленными
    return x % 1 == 0 and y % 1 == 0
