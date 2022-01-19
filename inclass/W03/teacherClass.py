class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        self.restaurants = []
        
    def add_restaurant(self,restaurants):
        self.restaurants.append(restaurants)

class Restaurant:
    def __init__(self, name, cuisine, price, rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

adam = Person("Adam Hayes")
print(adam)
print(adam.full_name)

heather = Person("Heather Purser")
print(heather)
print(heather.full_name)

aubury = Person("Aubury Orr")
print(aubury)
print(aubury.full_name)