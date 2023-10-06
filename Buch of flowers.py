
class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)
        self.set_life_time()

# при добавлении цветка в букет параллельно проставляем ему время жизни
    def set_life_time(self):
        for flower in self.flowers:
            setattr(flower, 'life_time', Flowers.get_life_time(flower))
        return flower.life_time


    def print_flowers(self):
        for flower in self.flowers:
            name = flower.name
            price = flower.price
            life_time = flower.life_time
            print(f'{name} : {price} byn, время жизни цветка {life_time}')

    # получение общей стоимости букета: (проходясь по словарю мы из каждого объекта вытягиваем значение ключа price)
    def get_total_price(self):
        total_price = 0
        for flower in self.flowers:
            price = flower.price
            total_price += price
        print(f'общая стоимость букета составляет {total_price} byn')


    #  метод высчитывания скорости увядания (в % в день) в зависимости от среднего времени жизни всех цветов в букете
    def average_life_time(self):
        total_life_time = 0
        for flower in self.flowers:
            total_life_time += flower.life_time
        average_life_time = total_life_time / len(self.flowers)
        withering_rate_of_flowers = 24 / average_life_time * 100  # 24 - изменяемая константа
        print(f'Среднее время жизни букета составляет {average_life_time} часов, скорость увядания букета составляет {withering_rate_of_flowers} % в сутки')

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
            if flower.color == color.lower():
                found_flowers.append(flower)

        if len(found_flowers) == 0:
            print("No flowers found with the specified color.")
        else:
            for flower in found_flowers:
                print(flower.name)


class Flowers:
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_lenght = stem_lenght

    def get_based_price(self):
        if self.freshness <= 50 or self.stem_lenght <= 50:  # в % и см
            based_price = 5
            return based_price
        elif 50 < self.freshness < 100 and 50 < self.stem_lenght <= 100:
            based_price = 10
            return based_price
        elif self.freshness == 100 and 50 < self.stem_lenght <= 100:
            based_price = 15
            return based_price

    def get_life_time(self):
        if self.freshness < 50:  # in %
            life_time = 24  # in hours
            return life_time
        elif 50 <= self.freshness < 100:
            life_time = 48
            return life_time
        else:
            life_time = 72
            return life_time




class Roses(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price()


    def get_price(self):
        based_price = self.get_based_price()
        if self.sort == "Dikson":
            price = based_price * 1.50
        elif self.sort == "Limbo":
            price = based_price * 1.80
        else:
            price = based_price * 0.9
        return price


class Tulips(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price()


    def get_price(self):
        based_price = self.get_based_price()
        if self.sort == "Triumf" and self.color == "Red":
            price = based_price * 1.50
        elif self.sort == "Darvin" and self.color == "Blue" or self.color == "Yellow":
            price = based_price * 1.80
        elif self.sort == "Queen":
            price = based_price * 2.0
        else:
            price = based_price * 0.85
        return price


class Pions(Flowers):
    def __init__(self, name: str, color: str, freshness: float, stem_lenght: float, sort: str):
        super().__init__(name, color, freshness, stem_lenght)
        self.sort = sort
        self.price = self.get_price()


    def get_price(self):
        based_price = self.get_based_price()
        if self.sort == "Baccara" and self.color == "Red":
            price = based_price * 1.50
        elif self.sort == "Ksander" and self.color == "Blue" or self.color == "Yellow":
            price = based_price * 1.80
        else:
            price = based_price * 0.85
        return price

if __name__ == "__main__":

    first_buch = Bouquet()
    first_buch.add_flowers(
        Roses(name='Lili', color='red', freshness=50, stem_lenght=75, sort='Limbo')
    )
    first_buch.add_flowers(
        Tulips(name='No_Barbie', color='yellow', freshness=60, stem_lenght=55, sort='Darvin')
    )
    first_buch.add_flowers(
        Pions(name='Sara', color='red', freshness=100, stem_lenght=100, sort='Ksander')
    )

    first_buch.print_flowers()
    first_buch.get_total_price()
    first_buch.average_life_time()
    first_buch.sort_by_color()
    first_buch.find_flower_by_color("BLUE")
    first_buch.sort_by_stem_lenght()
