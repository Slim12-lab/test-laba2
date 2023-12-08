class Game:
    def __init__(self):
        self.buildings = [Building('Пещера', 10.0, 1), Building('Торговая лавка', 100.0, 10.0),
                          Building('Магазин', 1000.0, 100.0), Building('Торговый центр', 10000.0, 1000.0),
                          Building('Завод', 100000.0, 10000.0), Building('SpaceX', 1000000.0, 100000.0),
                          Building('Земля', 10000000.0, 1000000.0)]
        self.player = Player()

    def check_win(self):
        if self.player.balance >= 1000000000:
            return True
        else:
            return False

    def buy(self, name):
        chosen = None
        for building in self.buildings:
            if building.name.lower() == name.lower():
                chosen = building
                break

        if not chosen:
            return 'Укажите корректное название недвижимости!'

        if self.player.balance < chosen.price:
            return 'Недостаточно средств!'

        self.player.minus_balance(chosen.price)
        chosen.add_building()
        self.player.add_income(chosen.income)

        return 'Удачная покупка!'


class Building:
    def __init__(self, name, price, income):
        self.name = name
        self.price = price
        self.income = income
        self.count = 0
        self.coef = 1.5

    def add_building(self):
        self.count += 1
        self.__multiply_price()
        return self.count

    def __multiply_price(self):
        self.price *= self.coef
        return self.price


class Player:
    def __init__(self):
        self.balance = 0
        self.income = 1

    def plus_balance(self):
        self.balance += self.income
        return self.balance

    def minus_balance(self, value):
        self.balance -= value
        return self.balance

    def add_income(self, income):
        self.income += income
        return self.income