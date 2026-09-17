try:
    L = int(input('введите рстояние в см: '))
    metr = L/100
    print(f'введенные {L} см. будут равны {metr} м.')
except:
    print('ошибка: Попробуй снова')