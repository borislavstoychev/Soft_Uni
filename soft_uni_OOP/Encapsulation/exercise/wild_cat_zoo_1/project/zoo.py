class Zoo:
    # Private attribute animal_capacity: number
    # Private attribute workers_capacity: number
    # Private attribute budget: number
    # Public attribute name: string
    # Public attribute animals: list (empty upon initialization)
    # Public attribute workers: list (empty upon initialization)
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price < self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if price > self.__budget:
            return f"Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_to_pay = sum(worker.salary for worker in self.workers)
        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_to_pay = sum(animal.get_needs() for animal in self.animals)
        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [str(lion) for lion in self.animals if lion.__class__.__name__ == "Lion"]
        tigers = [str(tiger) for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        cheetahs = [str(cheetahs) for cheetahs in self.animals if cheetahs.__class__.__name__ == "Cheetah"]
        if self.animals:
            n = "\n"
            return f"You have {len(self.animals)} animals\n" \
                   f"----- {len(lions)} Lions:\n" \
                   f"{n.join(lions)}\n" \
                   f"----- {len(tigers)} Tigers:\n" \
                   f"{n.join(tigers)}\n" \
                   f"----- {len(cheetahs)} Cheetahs:\n" \
                   f"{n.join(cheetahs)}"

    def workers_status(self):
        keepers = [str(keeper) for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        vets = [str(vet) for vet in self.workers if vet.__class__.__name__ == "Vet"]
        caretakers = [str(caretaker) for caretaker in self.workers if caretaker.__class__.__name__ == "Caretaker"]
        n = "\n"
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{n.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{n.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{n.join(vets)}"

