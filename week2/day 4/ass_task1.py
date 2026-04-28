class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    
phone1 = Phone("Tecno", "Pop10", 150000)
phone2 = Phone("Infinix", "Zero5", 120000)
phone3 = Phone("Samsung", "Galaxy S21", 200000)

print(phone1)
print(phone2)
print(phone3)