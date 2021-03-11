from project.cat import Cat


class Tomcat(Cat):
    _gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat._gender)

    @staticmethod
    def make_sound():
        return "Hiss"
