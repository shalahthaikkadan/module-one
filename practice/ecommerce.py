class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Warranty:", self.warranty)


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Size:", self.size)



class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Material:", self.material)



electronic = Electronics("Laptop", 50000, "2 Years")
clothing = Clothing("T-Shirt", 800, "L")
furniture = Furniture("Table", 5000, "Wood")



electronic.display()
print()

clothing.display()
print()

furniture.display()