# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_it(self):
        a = input("введите название товара")
        price = input("назначте цену")
        new_thng = {a : price}
        self.items.update(new_thng)


    def del_it(self):
        a = input("введите удаляемый товар")
        self.items.pop(a)


    def what_price(self):
        a = input("цена товара:")
        print(self.items.get(a))

    def renw_price(self):
        a = input("обновить цену для:")
        price = input("назначте цену")
        self.items.pop(a)
        new_thng = {a: price}
        self.items.update(new_thng)

shoes_shop = Store("Best-Shoes", "Москва")
toys_shop = Store("Happy Kids", "Пермь")
sport_shop = Store("Fitness", "Казань")

shoes_shop.items.update({"сапоги" : 1222, "туфли" : 1555, "кеды" : 1234})
toys_shop.items.update({"пупс" : 176, "заяц" : 555, "лего" : 8034})
sport_shop.items.update({"лыжи" : 17688, "ласты" : 6000, "мяч" : 500})

while True:
    print("\nвыберете магазин:")
    print(f"1 - {shoes_shop.name}")
    print(f"2 - {toys_shop.name}")
    print(f"3 - {sport_shop.name}")
    ch_shop = input()

    if ch_shop == "1":
        ch_shop = shoes_shop
    elif ch_shop == "2":
        ch_shop = toys_shop
    elif ch_shop == "3":
        ch_shop = sport_shop
    print(ch_shop.name, ch_shop.address, ch_shop.items.items())



    print("""   
     1 - для добавления товара в ассортимент
     2 - для удаления товара из ассортимента
     3 - для получения цены товара по его названию
     4 - для обновления цены товара
     0 - выход""")
    action = input()
    if action == "1":
        ch_shop.add_it()
    elif action == "2":
        ch_shop.del_it()
    elif action == "3":
        ch_shop.what_price()
    elif action == "4":
        ch_shop.renw_price()
    elif action == "0":
        break
    print(ch_shop.name, ch_shop.address, ch_shop.items.items())





