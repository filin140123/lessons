class PlayerInventory:
    def __init__(self, size):
        self.container = []
        self.size = size

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


# test case 1
pi1 = PlayerInventory(10)
pi1.list_items()
for i in range(10):
    pi1.append_item("stick")
pi1.list_items()
pi1.append_item("stick")
pi1.clear_inventory()
pi1.list_items()

print("-" * 30)

# test case 2
pi2 = PlayerInventory(20)
pi2.append_item("knife")
pi2.append_item("stone")
pi2.list_items()
pi2.discard_item("stone")
pi2.list_items()
