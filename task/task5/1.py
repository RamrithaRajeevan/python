#develop class product with attribute like name,price & quantity. Implement method to add to cart(adding quantity), remove from cart & calculate total cost.
class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_to_cart(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Added {amount} of {self.name} to the cart. Total quantity: {self.quantity}")
        else:
            print("Invalid amount to add")

    def remove_from_cart(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} of {self.name} from the cart. Total quantity: {self.quantity}")
        else:
            print("Invalid amount to remove")

    def calculate_total_cost(self):
        total_cost = self.quantity * self.price
        return total_cost

product = Product("mobile", 10000)
product.add_to_cart(3)  
product.remove_from_cart(1)  
print(f"Total cost: {product.calculate_total_cost()}")  
