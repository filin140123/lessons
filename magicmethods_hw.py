class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        print(f"Chain with {self.number_of_items} items")

    def __len__(self):
        return self.number_of_items
