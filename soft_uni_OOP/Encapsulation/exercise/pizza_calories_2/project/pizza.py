class Pizza:
    name: str
    # dough: Dough
    toppings = {}
    toppings_capacity = int

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings(self):
        return self.__toppings

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings.setter
    def toppings(self, values):
        self.__toppings = values

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_weight(self):
        total_weight = sum(topping for topping in self.__toppings.values()) + self.__dough.weight
        return total_weight

    def validate_topping_weight(self):
        return self.calculate_total_weight() <= self.__toppings_capacity

    def add_topping(self, topping):
        if topping.topping_type not in self.__toppings:
            if self.validate_topping_weight():
                self.__toppings[topping.topping_type] = topping.weight
            else:
                raise ValueError("Not enough space for another topping")
        else:
            if self.validate_topping_weight():
                self.__toppings[topping.topping_type] += topping.weight

