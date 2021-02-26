# from room import *

class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return Hotel(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= remove

    def print_status(self):
        fre_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        if fre_rooms:
            print(f"Free rooms: {', '.join(fre_rooms)}")
        if taken_rooms:
            print(f"Taken rooms: {', '.join(taken_rooms)}")





# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()