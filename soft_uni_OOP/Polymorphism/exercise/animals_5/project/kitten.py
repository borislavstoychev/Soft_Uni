from project.cat import Cat


class Kitten(Cat):
    _gender = "Female"

    def __init__(self, name, age):
        super(Kitten, self).__init__(name, age, Kitten._gender)

    @staticmethod
    def make_sound():
        return "Meow"
