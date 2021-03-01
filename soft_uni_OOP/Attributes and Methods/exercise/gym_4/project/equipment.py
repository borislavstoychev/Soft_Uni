class Equipment:

    id = 1

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Equipment <{Equipment.id}> {self.name}"

    @staticmethod
    def get_next_id():
        Equipment.id += 1
        return Equipment.id

