from abc import ABC, abstractmethod
from random import randint


class Person(ABC):
    def __init__(self, name, age, money, own_home=bool):
        self.name = name
        self.age = age
        self.money = money
        self.own_home = own_home

    @abstractmethod
    def show_info(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def buy_a_house(self):
        raise NotImplementedError('This method was not implemented')


class Human(Person):
    def show_info(self):
        print(f"Hey, my name is {self.name}. I'm {self.age} years old")
        if self.own_home:
            print("I have my own house!")
        else:
            print("I want to buy a house!")

    def make_money(self):
        self.money += 5000
        print(f"Your current balance is {self.money}")

    def buy_a_house(self, cost):
        if self.money >= cost:
            print("You just bought a new house! Congratulations!")
            self.own_home = True
        else:
            print("Sorry, you need to earn more money")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def house_info(self):
        print(f"The area of this house is {self.area}"
              f" and the price is {self.cost}")


class Home(House):
    def apply_discount(self, discount):
        self.cost *= discount


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def show_houses_info(self):
        print("Please see the available options:")
        for house in self.houses:
           house.house_info()

    def give_discount(self):
        return self.discount

    def steal_mony(self, person):
        if randint(1, 10) == 10:
            print("All your money has been stolen!")
            person.money = 0
        else:
            print("You are lucky guy!")

villa = Home("90m2", 30000)
town_home = Home("120m2", 50000)
mobile_home = Home("20m2", 5000)
houses = [villa, town_home, mobile_home]

tom = Human("Tom", "24", 40000, False)
bobbi_realtor = Realtor("Bobbi", houses, 0.9)

bobbi_realtor.show_houses_info()
bobbi_realtor.steal_mony(tom)

town_home_discount = bobbi_realtor.give_discount()
town_home.apply_discount(town_home_discount)
town_home.house_info()

tom.show_info()
tom.make_money()
tom.buy_a_house(villa.cost)



