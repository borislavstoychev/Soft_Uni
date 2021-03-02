class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub_id = [s for s in self.subscriptions if subscription_id == s.id][0]
        customer = [c for c in self.customers if sub_id.customer_id == c.id][0]
        trainer = [t for t in self.trainers if sub_id.trainer_id == t.id][0]
        ex_plan = [e for e in self.plans if e.id == sub_id.exercise_id][0]
        equipment = [eq for eq in self.equipment if ex_plan.equipment_id == eq.id][00]
        return f"{sub_id}\n{customer}\n{trainer}\n{equipment}\n{ex_plan}"
