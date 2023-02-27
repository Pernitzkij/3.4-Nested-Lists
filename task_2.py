participants = int(input('Кол-во участников: '))
tim = int(input('Кол-во человек в команде: '))
tim_list = []
num = 1

if participants % tim != 0:
    print(f'{participants} участников невозможно поделить на команды по {tim} человек!')
else:
    for i_tim in range(participants //tim ):
        tim_list.append(list(range(num, num + tim)))
        num += tim
    print(tim_list)