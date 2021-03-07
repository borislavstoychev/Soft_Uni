from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, price, milliliters, caffeine):
        super(Coffee, self).__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
