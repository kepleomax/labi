import random
def z1():
    a = list('14720')
    b = str(input("число"))
    if b in a:
        print (a,b,'угадали')
    else:
        print(a,b,'нет такого числа')

def z2():
    a = list('1234566789')
    s = set([v for v in a if a.count(v) > 1])
    if len(s) > 0:
        print(s)
    else:
        print ('отсутвуют')
def z3():
    a = ('пнд','втр','ср','чет','пят','суб','вос')
    b = input('сколько дней выхоных - ')
    c = len(a) - int(b)

    print(a[:c])
    print(a[c:])

def z4():
    a = ['Картошкин', 'Петров', 'Сидоров', 'Козявкин', 'Петрушин', 'Жаннафрискин', 'Пятачков', 'Сальцев',
         'Подтумбочкин', 'Мышков']
    b = ['Кулибин', 'Кокаколов', 'Беглов', 'Шторкин', 'Макуинов', 'Ссылочкин', 'Иванов', 'Курятин', 'Говядин',
         'Кролятин']
    c = random.randint(0,4)
    d = a[c:c-5]
    e = b[c:c+5]
    f = tuple(e+d)
    g = len(f)
    h = "Иванов" in f
    j = f.count("Иванов")
    k = sorted(f)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(j)
    print(k)
z1()
z2()
z3()
z4()
