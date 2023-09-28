from hiden_logic import get_based_price, get_life_time
import re


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def print_flowers(self):
        for flower in self.flowers:
            name = flower.name
            price = flower.price
            print(f'{name} : {price} byn')

    # получение общей стоимости букета: (проходясь по словарю мы из каждого объекта вытягиваем значение ключа price)
    def get_total_price(self):
        total_price = 0
        for flower in self.flowers:
            price = flower.price
            total_price += price
        return print(f'общая стоимость букета составляет {total_price} byn')

    # установление нового атрибута "время жизни цветка", которое рассчитывается из сторонней функции на основе его свежести
    def set_life_time(self):
        for flower in self.flowers:
            setattr(flower, 'life_time', get_life_time(flower.freshness))
        return flower.life_time

    #  метод высчитывания скорости увядания (в % в день) в зависимости от среднего времени жизни всех цветов в букете
    def average_life_time(self):
        total_life_time = 0
        for flower in self.flowers:
            total_life_time += flower.life_time
        average_life_time = total_life_time / len(self.flowers)
        withering_rate_of_flowers = 24 / average_life_time * 100  # 24 - изменяемая константа
        return print(
            f'Среднее время жизни букета составляет {average_life_time} часов, скорость увядания букета составляет {withering_rate_of_flowers} % в сутки')

    # сортировка по свежести
    def sort_by_freshness(self):
        sorted_objects = sorted(self.flowers, key=lambda flower: flower.freshness)
        for flower in sorted_objects:
            print(f'{flower.name} - {flower.freshness}')

    # сортировка по стоимости
    def sort_by_price(self):
        sorted_objects = sorted(self.flowers, key=lambda flower: flower.price)
        for flower in sorted_objects:
            print(f'{flower.name} - {flower.price}')

    # сортировка по длине стебля
    def sort_by_stem_lenght(self):
        sorted_objects = sorted(self.flowers, key=lambda flower: flower.stem_lenght)
        for flower in sorted_objects:
            print(f'{flower.name} - {flower.stem_lenght}')

    # сортировка по цвету
    def sort_by_color(self):
        sorted_objects = sorted(self.flowers, key=lambda flower: flower.color)
        for flower in sorted_objects:
            print(f'{flower.name} - {flower.color}')

    # поиск по цвету цветка в букете:
    def find_flower_by_color(self, color):
        found_flowers = []
        for flower in self.flowers:
            if re.search(color, flower.color, re.IGNORECASE):
                found_flowers.append(flower)

        if len(found_flowers) == 0:
            print("No flowers found with the specified color.")
        else:
            for flower in found_flowers:
                print(flower.name)
            return

class Flowers:
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_lenght = stem_lenght




class Roses(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price(self.sort, self.freshness, self.stem_lenght)


    def get_price(self, sort, freshness, stem_lenght):
        based_price = get_based_price(freshness=freshness, stem_lenght=stem_lenght)
        if sort == "Dikson":
            price = based_price * 1.50
        elif sort == "Limbo":
            price = based_price * 1.80
        else:
            price = based_price * 0.9
        return price


class Tulips(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price(self.sort, self.freshness, self.stem_lenght, self.color)


    def get_price(self, sort, freshness, stem_lenght, color):
        based_price = get_based_price(freshness=freshness, stem_lenght=stem_lenght)
        if sort == "Triumf" and color == "Red":
            price = based_price * 1.50
        elif sort == "Darvin" and color == "Blue" or color == "Yellow":
            price = based_price * 1.80
        elif sort == "Queen":
            price = based_price * 2.0
        else:
            price = based_price * 0.85
        return price


class Pions(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price(self.sort, self.freshness, self.stem_lenght, self.color)


    def get_price(self, sort, freshness, stem_lenght, color):
        based_price = get_based_price(freshness=freshness, stem_lenght=stem_lenght)
        if sort == "Baccara" and color == "Red":
            price = based_price * 1.50
        elif sort == "Ksander" and color == "Blue" or color == "Yellow":
            price = based_price * 1.80
        else:
            price = based_price * 0.85
        return price


if __name__ == "__main__":

    first_buch = Bouquet()
    first_buch.add_flowers(
        Roses(name='Lili', color='Red', freshness=50, stem_lenght=75, sort='Limbo')
    )
    first_buch.add_flowers(
        Tulips(name='No_Barbie', color='Yellow', freshness=60, stem_lenght=55, sort='Darvin')
    )
    first_buch.add_flowers(
        Pions(name='Sara', color='Red', freshness=100, stem_lenght=100, sort='Ksander')
    )

    first_buch.print_flowers()
    first_buch.get_total_price()
    first_buch.set_life_time()
    first_buch.average_life_time()
    first_buch.sort_by_color()
    first_buch.find_flower_by_color("blue")
