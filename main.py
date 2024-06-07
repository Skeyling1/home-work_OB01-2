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
        pass

    def what_price(self):
        pass

    def renw_price(self):
        pass

shoes_shop = Store("Best-Shoes", "Москва")
toys_shop = Store("Happy Kids", "Пермь")
sport_shop = Store("Fitness", "Казань")

shoes_shop.items.update({"сапоги" : 1222, "туфли" : 1555, "кеды" : 1234})
toys_shop.items.update({"пупс" : 176, "заяц" : 555, "лего" : 8034})
sport_shop.items.update({"лыжи" : 17688, "ласты" : 6000, "мяч" : 500})

shoes_shop.add_it()


print(shoes_shop.name)
print(shoes_shop.address)
print(shoes_shop.items.items())

