# 1. Basic Class and Object
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
         
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
      
    def fuel_type(self):
        return "Electric charge"

# my_car = Car("Toyota", "Corolla")
# print(my_car.get_brand())  # Output: Toyota !
# print(my_car.model)  # Output: Corolla

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)  # Output: Safari

# 2. Class Method and Self
print(my_new_car.full_name()) # Output: Tata Safari

# 3. Inheritance
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model) # Output: Model S
print(my_tesla.full_name()) # Output: Tesla Model S

# 4. Encapsulation
print(my_car.get_brand())  # Output: Toyota !

# 5. Polymorphism
print(my_tesla.fuel_type())  # Output: Electric charge
safari = Car("Tata", "Safari")
print(safari.fuel_type())  # Output: Petrol or Diesel

# 6. Class Variables

safari_three = Car("Tata", "Nexon")
print(safari.total_car) # 5

# 7. Static Method

my_car = Car("Suzuki", "Creta")
print(my_car.general_description())
print(Car.general_description())

# 8. Property Decorators

my_car.model = "City"
print(my_car.model) 
# AttributeError: property 'model' of 'Car' object has no setter

# 9. Class Inheritance and isinstance() Function

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# 10. Multiple Inheritance

class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"

class ElectricCarTwo(Battery, Engine, Car):
    pass
    
my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())