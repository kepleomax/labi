def z1(number:int):
    if number % 3 == 0:
        return True
    else:
        return False
print("pervoe zadanie")
print(z1(9))
print(z1(16))

def z2(number):
    res = 0
    try:
        if number == 0:
            raise ZeroDivisionError
        res = 100 /number
        return res
    except ValueError:
        print("нельзя использовать буквы")
    except ZeroDivisionError:
        print("нельзя делить на ноль")
print("vtoroe zadanie")
print(z2(1000))
print(z2(0))
def z3(date: str):
    date = date.split(".")
    if int(date[0]) * int(date[1]) == int(date[2][2:]):
        return True
    else:
        return False
print("tretie zadanie")
print (z3("02.02.2002"))
print (z3("04.12.2015"))

def z4(tic:str):
    l = len(tic)
    if l % 2 != 0:
        return False
    hl = l//2
    fl = sum(map(int,tic[:hl])) #значение строки выделяет на отдельные элементы и суммирует их
    sl = sum(map(int,tic[hl:]))
    if fl == sl:
        return True
print("chetvertoe zadanie")
print(z4("222222"))
print(z4("123456s"))