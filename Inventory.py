class Inventory:
    def __init__(self, name, price, quantity, supplier_name, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_name = supplier_name
