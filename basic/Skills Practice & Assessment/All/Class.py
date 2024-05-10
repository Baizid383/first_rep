class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"


my_dog = Dog("Tomy", 2)


print(f"My dog {my_dog.name} is {my_dog.age} years old.")
print("Dog says:", my_dog.bark())

class tom(Dog):
    def play(self):
        return "tom is playing!"
my_tom = tom("Max", 1)
print(f"My tom {my_tom.name} is {my_tom.age} year old.")
print("tom says:", my_tom.bark())
print(my_tom.play())




class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
account = BankAccount("123456", 1000)
print("Account Balance:", account.get_balance())




class Cat:
    def sound(self):
        return "Meow!"
class Duck:
    def sound(self):
        return "Quack!"
def animal_sound(animal):
    return animal.sound()
my_cat = Cat()
my_duck = Duck()
print("Cat says:", animal_sound(my_cat))
print("Duck says:", animal_sound(my_duck))


                                #Baizid#