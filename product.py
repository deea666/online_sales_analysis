class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(
            f"Produs: {self.name}, "
            f"Pret: {self.price} lei, "
            f"Cantitate: {self.quantity}"
        )

    def update_quantity(self, quantity):
        self.quantity = quantity
