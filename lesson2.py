def palidrom():
    stroka = input('Введите слово: ')
    palid = None
    index = 1
    stroka2 = ' ' + stroka
    for i in range(len(stroka) // 2):
        if stroka2[index] == stroka2[-index]:
            index += 1
            palid = True
        else:
            palid = False
            break
    if palid == True:
        print('True')
    elif palid == False:
        print('False')


palidrom()
