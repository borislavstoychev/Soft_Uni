class Account:

    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account: "Account", amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index: int):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __add__(self, other):
        new_acc = Account(owner=f"{self.owner}&{other.owner}", amount=self.amount+other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"


import unittest


class TestsAccount(unittest.TestCase):
    def setUp(self):
        self.acc1 = Account("Johhny")
        self.acc2 = Account("Anna", 40)

    def test_init(self):
        self.assertEqual(self.acc1.owner, "Johhny")
        self.assertEqual(self.acc1.amount, 0)
        self.assertEqual(self.acc1._transactions, [])
        self.assertEqual(self.acc2.owner, "Anna")
        self.assertEqual(self.acc2.amount, 40)
        self.assertEqual(self.acc2._transactions, [])

    def test_repr(self):
        self.assertEqual(repr(self.acc1), "Account(Johhny, 0)")

    def test_str(self):
        self.assertEqual(str(self.acc2), "Account of Anna with starting amount: 40")

    def test_add_transaction(self):
        self.acc1.add_transaction(10)
        self.assertEqual(self.acc1._transactions, [10])
        with self.assertRaises(ValueError) as cm:
            self.acc1.add_transaction(9.9)
        self.assertEqual(str(cm.exception), "please use int for amount")

    def test_balance(self):
        self.acc2.add_transaction(-20)
        self.assertEqual(self.acc2.balance, 20)

    def test_len(self):
        self.acc1.add_transaction(10)
        self.acc1.add_transaction(-5)
        self.assertEqual(len(self.acc1), 2)

    def test_get_item(self):
        self.acc1.add_transaction(5)
        self.assertEqual(self.acc1[0], 5)


if __name__ == "__main__":
    unittest.main()