from abc import abstractmethod, ABC

#Task 1

class Animals:
    def __init__(self, name, eat, sleep=int):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def speak(self):
        print(f"\nI'm {self.name}. I like to eat {self.eat}. I usually sleep for {self.sleep} hours")

    def go_to_sleep(self):
        print(f"......Sleeping for {self.sleep} hours........")

    def __str__(self):
        return self.name

animal = Animals('Animal', 'food', 10)
animal.speak()
animal.go_to_sleep()

class Bison(Animals):
    def __init__(self, name, eat, sleep=int, weight=int):
        super().__init__(name, eat, sleep)
        self.weight = weight

    def what_weight(self):
        print(f"My weight is {self.weight} kg")

bison = Bison('Bison', 'grass', 10, 1000)
bison.speak()
bison.what_weight()

class Leopard(Animals):
    def __init__(self, name, eat, sleep=int, speed=int):
        super().__init__(name, eat, sleep)
        self.speed = speed

    def how_fast(self):
        print(f"My speed is {self.speed} km per hour.")

leo = Leopard('Leo', 'meat', 15, 60)
leo.speak()
leo.how_fast()

class SnowLeopard(Leopard):
    def __init__(self, name, eat, color, sleep=int, speed=int):
        super().__init__(name, eat, sleep, speed)
        self.color = color

    def what_color(self):
        print(f"My color is {self.color}.")

snow_leo = SnowLeopard('Snow Leo', 'meat', 'white', 17, 55)
snow_leo.speak()
snow_leo.how_fast()
snow_leo.what_color()

class Hippo(Animals):
    def __init__(self, name, eat, sleep=int, hold_breath=int):
        super().__init__(name, eat, sleep)
        self.hold_breath = hold_breath

    def stay_underwater(self):
        print(f"I can stay underwater for up to {self.hold_breath} minutes.")

hippo = Hippo('Hippopotamus', 'fruits', 16, 5)
hippo.speak()
hippo.stay_underwater()

class Duck(Animals):
    def __init__(self, name, eat, sleep=int, fly_duration=int):
        super().__init__(name, eat, sleep)
        self.fly_duration = fly_duration

    def can_fly(self):
        print(f"I can fly for {self.fly_duration} hours.")

duck = Duck('Duck', 'fish', 13, 8)
duck.speak()
duck.can_fly()

print("\n Determine if each of the animal is an instance of the Animals class:")
creatures = (bison, leo, snow_leo, hippo, duck)

for creature in creatures:
    print(f"{creature} >", isinstance(creature, Animals))

#Task 1.a
print("-------------------------------------------------\n")

class Human:
    def __init__(self, name, eat, study, work, sleep=int):
        self.name = name
        self.eat = eat
        self.study = study
        self.work = work
        self.sleep = sleep

    def speak(self):
        print(f"\nI'm {self.name}. I like to eat {self.eat}. I usually sleep for {self.sleep} hours")

    def studying(self):
        print(f"I'm studying {self.study}")

    def working(self):
        print(f"I'm working as a {self.work}")

class Centaur(Human, Animals):
    def __init__(self, name, eat, study, work, weapon,  sleep=int):
        Animals.__init__(self, name, eat, sleep)
        Human.__init__(self, name, eat, study, work, sleep)
        self.weapon = weapon

    def fight(self):
        print(f"I'm fighting with a {self.weapon}")

centaur = Centaur('Ricki', 'vegitarian food', 'war', 'guard', 'knife', 6)
centaur.speak()
centaur.studying()
centaur.working()
centaur.fight()
centaur.go_to_sleep()

#Task 2

#a) Composition
print("-------------------------------------------------\n")

class Person:
    def __init__(self):
        right_arm = Arm(["thumb", "index finger", "middle finger", "ring finger", "pinkie"])
        left_arm = Arm(["thumb", "index finger", "middle finger", "ring finger", "pinkie"])
        self.arms = [right_arm.fingers, left_arm.fingers]

class Arm:
    def __init__(self, fingers):
        self.fingers = fingers

person = Person()
print(person.arms)

#b) Aggregation
print("-------------------------------------------------\n")

class CellPhone:
    def __init__(self, brand):
        self.brand = brand

class Screen:
    def __init__(self, brand_name, screen_type):
        self.brand_name = brand_name
        self.screen_type = screen_type

phone = CellPhone("iPhone")
screen = Screen(phone.brand, "LCD")
print(f"{screen.brand_name} has {screen.screen_type} screen")

#Task 3
print("-------------------------------------------------\n")

class DictMixin():
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes):
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class Profile(DictMixin):
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.sex = sex
        self.age = age
        self.birthday = birthday
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.last_name = last_name
        self.name = name

profile = Profile('Bob', 'Snail', '+38012345678', 'Mexico', 'bob.snail@gmail.com', 'December', '20', 'male')
print(profile.to_dict())

#Task 4
# Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
class LaptopInterface(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def webcam(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def ports(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError('This method was not implemented')

class HPLaptop(LaptopInterface):
    def __init__(self, screen_size, keyboard_type, touchpad_size, webcam_type, ports_availablity, dynamics_brand):
        self.screen_size = screen_size
        self.keyboard_type = keyboard_type
        self.touchpad_size = touchpad_size
        self.webcam_type = webcam_type
        self.ports_availablity = ports_availablity
        self.dynamics_brand = dynamics_brand

    def screen(self):
        print(f"The size of the screen is {self.screen_size}")

    def keyboard(self):
        print(f"Typy of keyboard is {self.keyboard_type}")

    def touchpad(self):
        print(f"Touchpad size is {self.touchpad_size} inch.")

    def webcam(self):
        print(f"Webcam type is {self.webcam_type}")

    def ports(self):
        print(f"What ports are avaialble: {self.ports_availablity}")

    def dynamics(self):
        print(f"Dynamics brand is: {self.dynamics_brand}")











