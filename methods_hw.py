class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = 0.0

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


ba1 = BankAccount(1, "a", "b")
print(ba1.balance)
ba1.add(50)
print(ba1.balance)
ba1.withdraw(15)
print(ba1.balance)
