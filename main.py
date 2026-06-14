from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 3500, 5)
product2 = Product("Mouse", 120, 10)
product3 = Product("Tastatura", 250, 8)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Lista produselor:")
manager.display_products()

print(
    f"\nValoarea totala a inventarului: "
    f"{manager.total_inventory_value()} lei"
)
