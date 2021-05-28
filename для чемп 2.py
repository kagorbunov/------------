
n = 'n'

whitebread = 0
blackbread = 0

while n == 'n':
    n = input('Введите n если пришло новое поступление или quit если рабочий день закончился :')
    if n == 'n':
        message = int(input('Введите 0 если хлеб белый или 1 если хлеб черный :'))
        if message == 0:
            num = input('Введите количество хлеба :')
            whitebread += int(num)
        elif message == 1:
            num = input('Введите количество хлеба :')
            blackbread += int(num)
    elif n == 'quit':
        print('')
        print('За день постпило: ')
        print('Буханок белого хлеба :', whitebread)
        print('Буханок черного хлеба :', blackbread)


