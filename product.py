class Product:  # Klasa Product zawierająca wartosci value

    def __init__(self, index, price, value1=0, value2=0, value3=0):
        self.index = index
        self.price = price
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __str__(self):
        return f"{self.index} {self.price} {self.value1} {self.value2} {self.value3}"