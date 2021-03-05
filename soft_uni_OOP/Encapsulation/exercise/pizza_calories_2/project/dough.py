class Dough:
    flour_type: str
    baking_technique: str
    weight: int

    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    @flour_type.setter
    def flour_type(self, value):
        self.__flour_type = value

    @baking_technique.setter
    def baking_technique(self, value):
        self.__baking_technique = value

    @weight.setter
    def weight(self, value):
        self.__weight = value


