# Lab: SOLID
Problems for in-class lab for the Python OOP Course @SoftUni.
## 1. Books - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/SOLID/lab/books.py)
Refactor the provided code, so there is a separate class called Library, which contains books and has a method called find_book(title) that returns the book with the given title. Remove the unnecessary code from the Book class.
```
class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page
```
## 2. Animals - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/SOLID/lab/animals.py)
Refactor the provided code, so you don't need to make any changes in it when you want to add new species to the animals list
```
class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
```
## 3. Robots - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/SOLID/lab/robots.py)
Refactor the provided code, so it is in line with the Liskov Substitution Principle. Define a method in the parent class. The subclasses should implement the method, so it returns the count of sensors for each type of robot.
```
class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type


class Android(Robot):
    def android_senzors_count(self):
        return 4


class Chappie(Robot):
    def chappie_senzors_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        if isinstance(robot, Android):
            print(robot.android_senzors_count())
        elif isinstance(robot, Chappie):
            print(robot.chappie_senzors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
```
## 4. Entertainment System - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/SOLID/lab/entertainment_system.py)
We've been hired to create a game where the player sets up entertainment systems. Each piece of the system (television, game console, etc.) uses a specific cable to connect to another device. The TV uses an HDMI cable to connect to a game console. Both the game console and TV connect to a router via an ethernet cable so they can access the internet. And lastly, all the devices are connected to the wall via a power cable so they can turn on. Your job is to extend this behavior in the device classes.
```
class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device): pass
    def connect_to_device_via_rca_cable(self, device): pass
    def connect_to_device_via_ethernet_cable(self, device): pass
    def connect_device_to_power_outlet(self, device): pass


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class dvd_player(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
```
## 5. Print books - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/SOLID/lab/print_books.py)
We want to be able to print books, but before printing the book we should be able to format it. To accomplish this we have a class that can print books called Printer and a class Formatter which is used by Printer. Refactor the provided code that breaks the DIP because both Printer and Formatter depend on concretions, not abstractions by creating some abstractions and inject them wherever they are needed.
```
class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book
```