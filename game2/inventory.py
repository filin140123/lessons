class PlayerInventory:
    def __init__(self, size):
        self.container = []
        self.size = size

    def __str__(self):
        counter = f"{len(self.container)}/{self.size}"
        if not self.container:
            return f"Empty, {counter}"
        return f"{self.container}, {counter}"

    def append_item(self, item):
        if len(self.container) < self.size:
            self.container.append(item)
        else:
            print("Inventory is full.")

    def discard_item(self, item):
        if item in self.container:
            self.container.remove(item)

    def clear_inventory(self):
        self.container = []

    def change_inventory_size(self, x: int):
        self.size += x

    def list_items(self):
        if not self.container:
            print("Inventory is empty.")
        else:
            for i in self.container:
                print(f"--- {i.title()}")
            if len(self.container) < self.size:
                print(f"{len(self.container)}/{self.size} empty slots left.")
            elif len(self.container) == self.size:
                print(f"{len(self.container)}/{self.size}, inventory is full.")


player_inventory = PlayerInventory(10)
