goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print(f'Текущий ассортимент:{goods}')
new_frute = [input('Новый фрукт: '), int(input("Цена: "))]
goods.append(new_frute)
print(f'Новый ассортимент:{goods}')
percent = int(input('введите добавочную стоимость в процентах: '))
for index in range(len(goods)):
    goods[index][1] += goods[index][1] * (percent / 100)
print(f'Новый ассортимент с увел. ценой:{goods}')
