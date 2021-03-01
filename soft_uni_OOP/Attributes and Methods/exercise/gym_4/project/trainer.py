class Trainer:

    id = 1

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        Trainer.id += 1
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{Trainer.id}> {self.name}"

