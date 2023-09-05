class Items:
    def __init__(self, name, price, initial_amount):
        self.name = name
        self.price = price
        self.amount = initial_amount
        self.profit = 0

    def sell(self, amount_sold):
        if amount_sold <= self.amount:
            self.amount -= amount_sold
            revenue = self.price * amount_sold
            self.profit += revenue
            return revenue
        else:
            return 0

    def remaining_amount(self):
        return self.amount

    def current_profit(self):
        return self.profit

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_profit(self):
        return sum(product.current_profit() for product in self.products)

    def save_state(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                file.write(f"{product.name},{product.price},{product.amount},{product.profit}\n")

    def load_state(self, filename):
        self.products = []
        with open(filename, 'r') as file:
            for line in file:
                name, price, amount, profit = line.strip().split(',')
                product = Items(name, float(price), int(amount))
                product.profit = float(profit)
                self.products.append(product)

product1 = Items("Boots", 50.0, 10)
product2 = Items("Coat", 80.0, 8)
product3 = Items("Scarf", 20.0, 20)

store = Shop()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

revenue1 = product1.sell(5)
revenue2 = product2.sell(4)
revenue3 = product3.sell(15)

print(f"There are {product1.remaining_amount()} units of {product1.name} left")
print(f"Profit for {product1.name}: {product1.current_profit()}$")
print(f"There are {product2.remaining_amount()} units of {product2.name} left")
print(f"Profit for {product2.name}: {product2.current_profit()}$")
print(f"There are {product3.remaining_amount()} units of {product3.name} left")
print(f"Profit for {product3.name}: {product3.current_profit()}$")
print(f"Total: {store.total_profit()}$")

store.save_state("store_state.txt")

store.load_state("store_state.txt")
