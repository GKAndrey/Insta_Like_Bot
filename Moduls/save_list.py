def get_list():
    lst = []
    chec = input('''Введите ссылки постов, под которыми желаете поставить лайкк.
Можете скинуть их одной строкой через запятые(,) или добовлять по очереди.
Чтоб закончить ввод напишите 0.\n''')
    chec.split()
    if chec == "0":
        print("Неудачная попытка, список пуст.")
    else:
        while chec != "0":
            if chec == "0 " or chec == "0  ":
                break
            chec = chec.split()
            for i in chec:
                lst.append(i)
            chec = input()
    return lst
