class Car:
    company=0
    price=0
    color=0
    def cars(self):
        print("Company:",self.company)
        print("Price:",self.price)
        print("Colour:",self.color)
        print()
        print()
        
car1=Car()
car1.company="BMW"
car1.price=5000000
car1.color="RoyalBlue"
print("Car details of first car:")
car1.cars()



car2=Car()
car2.company="Audi"
car2.price=4500000
car2.color="Red"
print("Car details of second car:")
car2.cars()


car3=Car()
car3.company="Mini Cooper"
car3.price=5500000
car3.color="Green"
print("Car details of third car:")
car3.cars()
