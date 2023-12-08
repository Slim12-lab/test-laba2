# This is a sample Python script.
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':  # pragma: no cover
    game = Game()
    print("Игра \"Миллиардер\"\nКоманды:\n1. Баланс, доход и недвижимость: stat\n2. Магазин: store\n3. Работать: work\n4. Команды: help\n5. Выйти: quit")
    while True:
        if (game.check_win()):
            "Вы стали миллиардером!"
            quit()
        command = input()
        if command == 'stat':
            print("Баланс: " + str(game.player.balance))
            print("Доход: " + str(game.player.income) + "$")
            print("Недвижимость: ")
            for building in game.buildings:
                building_str = building.name
                while len(building_str) < 30 - len(str(building.count)):
                    building_str += " "
                print(building_str + str(building.count))

        elif command =="store":
            print("Магазин\n")
            for building in game.buildings:
                building_str = building.name
                while len(building_str) < 30 - len(str(building.price)):
                    building_str += " "
                print(building_str + str(building.price) + "$")

            while True:
                print("\nВведите название недвижимости, чтобы купить её, или back, чтобы выйти из меню покупки:")
                temp = input()
                if (temp == 'back'):
                    print("Вы отказались от покупки!")
                    break
                print(game.buy(temp))
        elif command == "work":
            print("+" + str(game.player.income) + "$")
            print("Баланс: " + str(game.player.plus_balance()) + "$")
        elif command == "help":
            print( "Команды:\n1. Баланс, доход и недвижимость: stat\n2. Магазин: store\n3. Работать: work\n4. Команды: help\n5. Выйти: quit")
        elif command == "quit":
            quit()
        else:
            print("Вы ввели некорректную команду! Попробуйте ещё раз.")

