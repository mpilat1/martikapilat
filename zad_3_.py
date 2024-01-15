class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, plot size {self.plot} sqm"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, on floor {self.floor}"

# Tworzenie obiektu klasy House
house = House(200, 5, "500,000 USD", "123 Main St", 1500)

# Tworzenie obiektu klasy Flat
flat = Flat(80, 3, "300,000 USD", "456 Elm St", 2)

# Wyświetlanie obiektów
print(house)
print(flat)
