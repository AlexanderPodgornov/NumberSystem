# писал в 2019 (5 лет назад)

import sys
import math

ch = input('Введите число = ')
s1 = int(input('Введите систему счисления этого числа (максимум 36) = '))
s2 = int(input('Введите систему счисления, в которую нужно перевести это число = '))
dl = len(ch)
dotx = []
asd = 0
znak = 0  # проверка на строка.число
flag = 0  # разделение на тип задачи
for i in ch:
    if i == '.':
        asd = asd + 1
if asd > 1:
    print()
    print('ОШИБКА!')
    sys.exit()
if '.' in ch and (s1 > 10 or s2 > 10):
    znak = 1
if znak == 0:
    try:
        if s1 <= 10 and float(ch) - math.ceil(float(ch)) == 0 and znak == 0:
            ch = int(ch)
            t = ch
            flag = 1
        if s1 <= 10 and znak == 0:
            if float(ch) - math.floor(float(ch)) > 0 and znak == 0:
                flag = 3
                ch = float(ch)
                t = ch
        if s1 > 10 and znak == 0:
            if '.' in ch:
                dotx = str(ch).split('.')
        if s1 > 10:
            flag = 2
            ch = str(ch)
    except ValueError:
        print('ОШИБКА!')
        sys.exit()
if s2 > 36:
    print()
    print('ОШИБКА!')
    sys.exit()
if s2 == s1:
    print('Зачем?')
    sys.exit()
if 1 == 1:
    tx1 = []  # цифры числа до точки
    tx2 = []  # цифры числа после точки (z)
    ty1 = 0  # число до точки
    ty2 = 0  # число после точки
    a = []
    znam1x = 0  # сокращенный знаменатель дроби строка.число
    chislx = 0  # сокращенный числитель дроби строка.число
    znam = []  # знаменатели после запятой
    chis = []
    Chis = []  # массив чисел в числителе обыкновенной дробью
    sum_Chis = 0  # ответ в числителе обыкновенной дробью (не сокр.)
    sum_chis = 0
    sum_Chisx = 0  # ответ в числителе обыкновенной дробью ( сокр.)  число.число
    nokx = 0  # ответ в знаменателе обыкновенной дробью ( сокр.) число.число
    nok = 0  # znam[-1] ответ в знаменателе обыкновенной дробью ( не сокр.)
    znamen = 0
    chisl = 0
    h = 0
    b = []
    t1 = 0
    y1 = 0
    y2 = 0
    y3 = 0  # копия ответа для flag == 2
    y4 = 0  # копия ответа для flag == 2
    t0 = 0
    mas = []
    znam1 = []  # знаменатели строка.число
    dot = []  # список из 2 чисел - до и после точки
    string_alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # A = 10     Z = 36     номер буквы + 10
    g = 0  # ответ для 2-10  --> 10
    y = 0  # ответ для 11-36 --> 10
    d = 0  # ответ для дробных чисел 2-10 --> 10
    yx = 0  # ответ для строка.число
    ost = []  # остатки при делении
    cel = []  # целые части от деления
    nomer = 0
    g1 = 0
    gx = 0  # ответ для s2 системы счисления   число
    f = 1  # умножение на 10  -  переворот списка
    gxstr = 0
    cely = []
    nomery = 0
    osty = []
    ystr = 0
    doty = []
    doty1 = 0
    doty2 = 0
    doty3 = 0
    doty4 = 0
    doty5 = 0
    doty6 = 0
    dotyx = []
    dotyo = 0
    nomerx = 0
    ostspis = []
    spisok = []
    txx = []
    celx = 0
    xxx = 1
    doty7 = []
    doty10 = []
    doty11 = []
    xx = 0
    celt = []
    yy = 0
    stryy = 0
    stryy1 = 0
    otvx = 0
    z = []
    zz = []
    rf = []
    nomeru = 0
    ostu = []
    des = 1
    otvet = 0
    df = []
    df1 = 0
    u = 0
if flag == 1 and znak == 0:
    while t > 0:
        a.append(t % 10)
        t = t // 10
    a.reverse()  # список цифр в числе
    for i in range(len(a)):
        h = a[i] * (s1 ** (len(a) - i - 1))
        b.append(h)  # результаты каждого возведения в степень
        g = h + g
    # print(a) цифры начального числа
    if max(a) >= s1 or s1 <= 0 or s2 <= 0 or ch < 0:
        print('ОШИБКА!')
        sys.exit()
    if s2 == s1:
        print()
        print('Зачем?')
        sys.exit()
if flag == 2 and znak == 0:
    y3 = y
    y4 = y
    try:
        y = int(ch, s1)
    except ValueError:
        print("ОШИБКА!")
        sys.exit()
    # print()
if flag == 3 and znak == 0:
    dot = str(ch).split('.')
    t0 = int(dot[0])
    t1 = list(dot[1])
    #  print(t1)
    #  print(type(t1))
    for i in range(len(t1)):
        z.append(int(t1[i]))
    # print(z)
    # print(type(z[0]))
    # print('t0 =', t0)
    if t0 == 0:
        tx1.append(0)
    if t0 != 0:
        while t0 > 0:
            tx1.append(t0 % 10)
            t0 = t0 // 10
        tx1.reverse()
    for i in range(len(tx1)):
        ty1 = ty1 + (tx1[i] * (s1 ** (len(tx1) - i - 1)))  # до точки
    for i in range(len(z)):
        ty2 = ty2 + (z[i] * (s1 ** (-i - 1)))  # после точки
        znam.append((s1 ** abs(-i - 1)))
    nok = znam[-1]
    for i in range(len(znam)):
        chis.append(math.floor(nok / znam[i]))
    for i in range(len(chis)):
        Chis.append(z[i] * chis[i])
    sum_Chis = sum(Chis)
    d = ty1 + ty2
    # print(tx1)
    # print(z)
    if max(max(tx1), max(z)) >= s1:
        print()
        print('ОШИБКА!')
        sys.exit()
    if s1 == s2:
        print()
        print('Зачем?')
        sys.exit()
    for i in range(1, sum_Chis):
        if sum_Chis % i == 0 and znam[-1] % i == 0:
            nokx = znam[-1] / i
            sum_Chisx = sum_Chis / i
    sum_Chisx = math.floor(sum_Chisx)
    nokx = math.floor(nokx)
    print()
    if nokx == znam[-1] and sum_Chisx == sum_Chis:
        print(ch, '(', s1, ')', '=', d, '( 10 )', ' = ', math.floor(d), '(', sum_Chis, '/', nok, ')', '( 10 )')
    else:
        print(ch, '(', s1, ')', '=', d, '( 10 )', ' = ', math.floor(d), '(', sum_Chisx, '/', nokx, ')', '( 10 )')
    # print(sum_Chis)
    # print(znam[-1])
if znak == 1:
    dot = ch.split('.')
    try:
        y1 = int(dot[0], s1)  # ответ до точки
        for i in dot[1]:
            mas.append(int(i, s1))
        for i in range(len(mas)):
            y2 = y2 + (mas[i] * (s1 ** (-i - 1)))
        yx = y1 + y2
    except ValueError:
        print()
        print('ОШИБКА!')
        sys.exit()
    for i in range(len(mas)):
        znam1.append(s1 ** (abs(-i - 1)))
    for i in range(len(mas)):
        chisl = chisl + mas[i] * znam1[-1] / znam1[i]
    chisl = math.floor(chisl)
    for i in range(1, chisl):
        if chisl % i == 0 and znam1[-1] % i == 0:
            chislx = chisl / i
            znam1x = znam1[-1] / i
    chislx = math.floor(chislx)
    znam1x = math.floor(znam1x)
    print()
    if chislx == chisl and znam1x == znam1[-1]:
        print(ch, '(', s1, ')', '=', yx, '( 10 )', ' = ', math.floor(yx), '(', chisl, '/', znam1[-1], ')', '( 10 )')
    else:
        print(ch, '(', s1, ')', '=', yx, '( 10 )', ' = ', math.floor(yx), '(', chislx, '/', znam1x, ')', '( 10 )')
if flag == 1 and znak == 0:
    g1 = g
    g2 = g
    while g / s2 > 0:
        cel.append(g // s2)
        g = g // s2
        nomer += 1
    for i in range(nomer):
        ost.append(g1 - (cel[i] * s2))
        g1 = cel[i]
    for i in range(nomer):
        gx = gx + ost[i] * f
        f = f * 10
    ost.reverse()
    for i in range(len(ost)):
        if ost[i] >= 10:
            ost[i] = chr(ost[i] + 55)
            ost[i] = str(ost[i])
    gxstr = ''.join(map(str, ost))
    print()
    print(ch, '(', s1, ')', '=', g2, '( 10 )', '=', gxstr, '(', s2, ')')
if flag == 2 and znak == 0:
    y3 = y
    y4 = y
    while y / s2 > 0:
        cely.append(y // s2)
        y = y // s2
        nomery += 1
    for i in range(nomery):
        osty.append(y3 - (cely[i] * s2))
        y3 = cely[i]
    osty.reverse()
    for i in range(len(osty)):
        if osty[i] >= 10:
            osty[i] = str(chr(osty[i] + 55))
    ystr = ''.join(map(str, osty))
    print()
    print(ch, '(', s1, ')', '=', y4, '( 10 )', '=', ystr, '(', s2, ')')
    # print(cely)
    # print(osty)
    # print(ystr)
if flag == 3 and znak == 0:
    d1 = d
    d2 = d
    razx = 0
    doty = str(d).split('.')
    doty1 = int(doty[0])
    doty2 = list(doty[1])
    for i in range(len(doty2)):
        zz.append(int(doty2[i]))
    doty3 = doty1
    doty4 = doty2
    doty5 = doty1
    doty6 = doty2
    #  print(doty1)
    while doty1 > 0:
        txx.append(doty1 % 10)
        doty1 = doty1 // 10
    txx.reverse()
    #  print('txx = ', txx)
    while doty3 / s2 > 0:
        ostspis.append(doty3 // s2)
        doty3 = doty3 // s2
        nomerx += 1
    #  print(doty5)
    #  print('ostspis = ', ostspis)
    #  print('nomerx = ', nomerx)
    if doty5 == 0:
        spisok.append(0)
    if doty5 != 0:
        for i in range(nomerx):
            spisok.append(doty5 - s2 * ostspis[i])
            doty5 = doty5 // s2
            spisok[i] = str(spisok[i])
        #  print('spisok = ', spisok)  # str
        spisok.reverse()
    #  print(spisok)
    celx = ''.join(map(str, spisok))
    #  print('celx')
    #  print('celx = ', celx) # целая часть ответа
    #  print('doty6 = ', doty6)  # дробная часть (не ответ)
    xx = doty6
    for i in range(len(zz)):
        zz[i] = int(zz[i])
    for i in range(len(zz)):
        zc = ''.join(str(zz))
    # print(int(str('001')))
    # print(type(int(str('001'))))
    #  print('zc =', zc)
    d1 = d
    d = str(d)
    cf = d.split('.')
    raz = round(d1 - math.floor(d1), len(cf[1]))
    # print('raz = ', raz)  # важно
    # print(doty6)
    # print('type(raz) = ', type(raz))
    while raz != 0 and u < 100:  # тут изменять
        #  print(raz)
        yy = float(raz) * s2  # == 0
        # print('yy = ', yy)
        # print('type(yy) = ', type(yy))
        stryy = str(yy)
        # print('stryy = ', stryy)
        # print('len = ', len(stryy)-2)
        # print('doty6 = ', doty6)
        if stryy == 0:
            break
        if float(stryy) < 1:
            stryy1 = 0
        if float(stryy) >= 1:
            stryy1 = stryy[0]
            stryy = stryy[1:]
        celt.append(stryy1)
        raz = stryy
        u = u + 1
        if raz == '0.0' or raz == '.0':
            break
    #  print(celt)
    r = ''.join(map(str, celt))  # дробная часть (ответ
    otvx = celx + '.' + str(r)
    print(ch, '(', s1, ')', ' = ', otvx, '(', s2, ')')
    #  print(otvx)  # ответ для число.число
if znak == 1:
    yx1 = str(yx)
    z1 = yx1.split('.')
    zotv = int(z1[0])
    zotv1 = zotv
    zotv2 = zotv
    while zotv / s2 > 0:
        rf.append(zotv // s2)
        zotv = zotv // s2
        nomeru += 1
    #  print(rf)
    for i in range(nomeru):
        ostu.append(zotv1 - (rf[i] * s2))
        zotv1 = rf[i]
    for i in range(nomeru):
        gx = gx + ostu[i] * des
        des = des * 10
    ostu.reverse()
    for i in range(len(ostu)):
        if ostu[i] >= 10:
            ostu[i] = chr(ostu[i] + 55)
        ostu[i] = str(ostu[i])
    if len(ostu) == 0:
        ostu.append('0')
    otvet = ''.join(ostu)
    #  print(otvet, '=====')  # важно
    #  print(type(yx))
    df = yx1.split('.')
    df1 = round(yx - math.floor(yx), len(df[1]))
    while df1 != 0 and u < 100:  # тут изменять
        yy = float(df1) * s2  # == 0
        # print('yy = ', yy)
        # print('type(yy) = ', type(yy))
        stryy = str(yy)
        # print('stryy = ', stryy)
        # print('len = ', len(stryy)-2)
        # print('doty6 = ', doty6)
        #  print(stryy)
        if stryy == 0:
            break
        if float(stryy) < 1:
            stryy1 = 0
        if 1 < float(stryy) < 10:
            stryy1 = stryy[0]
            stryy = stryy[1:]
        if 36 >= float(stryy) >= 10:
            stryy1 = stryy[0] + stryy[1]
            stryy = stryy[2:]
        celt.append(stryy1)
        df1 = stryy
        u = u + 1
        #  print(df1)
        if df1 == '0.0' or df1 == '.0':
            break
    #  print(celt)
    for i in range(len(celt)):
        celt[i] = int(celt[i])
    for i in range(len(celt)):
        if celt[i] >= 10:
            celt[i] = chr(celt[i] + 55)
    r = ''.join(map(str, celt))  # дробная часть (ответ)
    otvx = otvet + '.' + str(r)
    print(ch, '(', s1, ')', ' = ', otvx, '(', s2, ')')

