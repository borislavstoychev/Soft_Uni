# from dvd import *
# from customer import *


class MovieWorld:

    def __init__(self,  name: str):
        self.name = name
        self.customers = []
        self.dvds = []
        self.dvds_id = {}
        self.customers_id = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if not len(self.customers) >= self.customer_capacity():
            self.customers.append(customer)
            self.customers_id[customer.id] = customer

    def add_dvd(self, dvd):
        if not len(self.dvds) >= self.dvd_capacity():
            self.dvds.append(dvd)
            self.dvds_id[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_name = self.dvds_id.get(dvd_id)
        customer_name = self.customers_id.get(customer_id)
        if dvd_name in customer_name.rented_dvds:
            return f"{customer_name.name} has already rented {dvd_name.name}"
        if dvd_name.is_rented:
            return "DVD is already rented"
        if customer_name.age < dvd_name.age_restriction:
            return f"{customer_name.name} should be at least {dvd_name.age_restriction} to rent this movie"
        customer_name.rented_dvds.append(dvd_name)
        dvd_name.is_rented = True
        return f"{customer_name.name} has successfully rented {dvd_name.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd_name = self.dvds_id.get(dvd_id)
        customer_name = self.customers_id.get(customer_id)
        if dvd_name in customer_name.rented_dvds:
            dvd_name.is_rented = False
            customer_name.rented_dvds.remove(dvd_name)
            return f"{customer_name.name} has successfully returned {dvd_name.name}"
        return f"{customer_name.name} does not have that DVD"

    def __repr__(self):
        movies = list(map(str, self.dvds))
        customers = list(map(str, self.customers))

        return "\n".join(customers + movies)


