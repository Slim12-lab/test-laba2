from clicker import Game, Building, Player
import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    # integration tests

    def test_buy_unsufficient_balance(self):
        self.game.player.balance = 0
        self.game.player.income = 1
        self.assertEqual(self.game.buy('пещера'), 'Недостаточно средств!')
        self.assertEqual(self.game.player.balance, 0)
        self.assertEqual(self.game.player.income, 1)
        self.assertEqual(self.game.buildings[0].count, 0)
        self.assertEqual(self.game.buildings[0].price, 10.0)

    def test_buy_sufficient_balance(self):
        self.game.player.balance = 10
        self.game.player.income = 1
        self.assertEqual(self.game.buy('пещера'), 'Удачная покупка!')
        self.assertEqual(self.game.player.balance, 0)
        self.assertEqual(self.game.player.income, 2)
        self.assertEqual(self.game.buildings[0].count, 1)
        self.assertEqual(self.game.buildings[0].price, 15.0)

    def test_buy_wrong_name(self):
        self.game.player.balance = 0
        self.game.player.income = 1
        self.assertEqual(self.game.buy('пещераааааааа'), 'Укажите корректное название недвижимости!')
        self.assertEqual(self.game.player.balance, 0)
        self.assertEqual(self.game.player.income, 1)
        self.assertEqual(self.game.buildings[0].count, 0)
        self.assertEqual(self.game.buildings[0].price, 10.0)

    def test_check_win_positive(self):
        self.game.player.balance = 1000000000
        self.assertEqual(self.game.check_win(), True)

    def test_check_win_negative(self):
        self.game.player.balance = 1
        self.assertEqual(self.game.check_win(), False)


class TestBuilding(unittest.TestCase):
    def setUp(self):
        self.building = Building('Пещера', 10, 1)

    def test_add_building(self):
        self.assertEqual(self.building.add_building(), 1)
        self.assertEqual(self.building.price, 15.0)

    def test_multiply_price(self):
        self.assertEqual(self.building._Building__multiply_price(), 15.0)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_plus_balance(self):
        self.assertEqual(self.player.plus_balance(), 1)

    def test_minus_balance(self):
        self.player.balance = 1
        self.assertEqual(self.player.minus_balance(1), 0)

    def test_add_income(self):
        self.assertEqual(self.player.add_income(1), 2) 

if __name__ == "__main__": 
    unittest.main()
