[![Coverage Status](https://coveralls.io/repos/github/Slim12-lab/test-laba2/badge.svg?branch=main)](https://coveralls.io/github/Slim12-lab/test-laba2?branch=main)
[![CI/CD GitHub Actions](https://github.com/Slim12-lab/test-laba2/actions/workflows/test_action.yml/badge.svg)](https://github.com/Slim12-lab/test-laba2/actions/workflows/test_action.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Slim12-lab_test-laba2&metric=alert_status)](https://sonarcloud.io/dashboard?id=Slim12-lab_test-laba2&metric=alert_status)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Slim12-lab_test-laba2&metric=bugs)](https://sonarcloud.io/project/issues?resolved=false&types=BUG&sinceLeakPeriod=true&id=Slim12-lab_test-laba2)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Slim12-lab_test-laba2&metric=code_smells)](https://sonarcloud.io/project/issues?resolved=false&types=CODE_SMELL&sinceLeakPeriod=true&id=Slim12-lab_test-laba2)
# План тестирования: 
 
# Аттестационное тестирование
  - Тест А1 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь запускает программу
    - Ожидаемый результат:
        ```
      Игра "Миллиардер"
      Команды:
      1. Баланс, доход и недвижимость: stat
      2. Магазин: store
      3. Работать: work
      4. Команды: help
      5. Выйти: quit
  - Тест А2 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь запускает программу и вводит "stat"
    - Ожидаемый результат: 
      ```                  
     	  Баланс: 0
        Доход: 1$
        Недвижимость: 
        Пещера                       0
        Торговая лавка               0
        Магазин                      0
        Торговый центр               0
        Завод                        0
        SpaceX                       0
        Земля                        0
      ```                         
  - Тест А3 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь запускает программу и вводит "store"
    - Ожидаемый результат: 
        ```
         Магазин

         Пещера                    10.0$
         Торговая лавка           100.0$
         Магазин                 1000.0$
         Торговый центр         10000.0$
         Завод                 100000.0$
         SpaceX               1000000.0$
         Земля               10000000.0$

         Введите название недвижимости, чтобы купить её, или back, чтобы выйти из меню покупки:
        ```                               
  - Тест А4 (положительный)
    - Начальное состояние: Открытый терминал, введённая команда store, баланс = 10</li>
    - Действие: Пользователь вводит "пещера"</li>
    - Ожидаемый результат: 
        ```                       
      Удачная покупка!
        ```          
  - Тест А5 (положительный)
    - Начальное состояние: Открытый терминал, доход = 1, баланс = 0</li>
    - Действие: Пользователь запускает программу, вводит "work"</li>
    - Ожидаемый результат: 
        ```                       
       +1
        Баланс: 1
        ```        
  - Тест А6 (положительный)
    - Начальное состояние: Открытый терминал</li>
    - Действие: Пользователь запускает программу, вводит "help"</li>
    - Ожидаемый результат: 
        ```                       
      Команды:
      1. Баланс, доход и недвижимость: balance
      2. Магазин: store
      3. Работать: work
      4. Команды: help
      5. Выйти: quit 
  - Тест А6 (положительный)
    - Начальное состояние: Открытый терминал</li>
    - Действие: Пользователь запускает программу, вводит "quit"</li>
    - Ожидаемый результат: 
        ```
        * Программа закрылась *
# Блочное тестирование
## Класс Building
<ol>
  <li>
    <h3>Метод add_building()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б1.1 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: self.count = 0, self.price = 10.0, self.coef = 1.5</li>
    	    <li>Ожидаемый результат: self.count = 1, self.price = 15.0 </li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод __multiply_price()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б1.2 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: self.price = 10.0, self.coef = 1.5</li>
    	    <li>Ожидаемый результат: self.price = 15.0</li>
    	  </ul>
    	</li>
    </ol>
  </li>
</ol>

## Класс Player

<ol>
  <li>
    <h3>Метод plus_balance()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.1 (положительный)</h4>
    	  <ul>
            <li>Входные данные: self.balance = 0, self.income = 1</li>
    	    <li>Ожидаемый результат: self.balance = 1</li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод minus_balance(value)</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.2 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: value = 1, self.balance = 1</li>
    	    <li>Ожидаемый результат: self.balance = 0</li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод add_income(income)</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.3 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: income = 1, self.income = 1</li>
    	    <li>Ожидаемый результат: self.income = 2</li>
    	  </ul>
    	</li>
    </ol>
  </li>
</ol>

# Интеграционное тестирование
<ol>
  <li>
    <h3>Тест И1</h3>
    <ul>
      <li>Методы: Game.buy(), Player.minus_balance(), Building.add_building(), Player.add_income()</li>
      <li>Описание: Успешная покупка недвижимости игроком </li>
      <li>Входные данные: 
            player.balance = 10,
            building.price = 10,
            building.coef = 1.5,
            building.count = 0,
            player.income = 1
      </li>
      <li>Ожидаемый результат: 
        player.balance = 0, 
        building.price = 15.0,
        building.count = 1, 
        player.income = 2,
        return "Удачная покупка!"
      </li>
    </ul>	
  </li>
  <li>
    <h3>Тест И2</h3>
    <ul>
      <li>Методы: Game.buy(), Player.minus_balance(), Building.add_building(), Player.add_income()</li>
      <li>Описание: Неудачная покупка недвижимости игроком </li>
      <li>Входные данные: 
            player.balance = 0,
            building.price = 10,
            building.coef = 1.5,
            building.count = 0,
            player.income = 1
      </li>
      <li>Ожидаемый результат: 
        player.balance = 0, 
        building.price = 10,
        building.count = 0, 
        player.income = 1,
        return "Недостаточно средств!"
      </li>
    </ul>	
  </li>

</ol>

