# This is a sample Python script.
import re
from clicker import Game, Building, Player

if __name__ == '__main__': #pragma: no cover
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

