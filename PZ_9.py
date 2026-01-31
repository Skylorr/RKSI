#Определить в каких магазинах можно приобрести книги Маяковского

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
buk_market = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

shops = {
    'Магистр': magistr,
    'ДомКниги': dom_knigi,
    'БукМаркет': buk_market,
    'Галерея': galereya
}

author = 'Маяковский'

print(f'Книги {author} можно купить в магазинах:')

for shop, authors in shops.items():
    if author in authors:
        print(shop)