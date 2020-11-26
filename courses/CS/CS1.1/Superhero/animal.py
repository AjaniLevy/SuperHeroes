class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))
    def eat(self):
        print (f"{self.name} is eating")
    def drink(self):
        print (f"{self.name} is drinking")
class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping right this moment")

Pine = Animal("Jake", 12)
Geoffery = Frog("James", 45)
Geoffery.jump()
Pine.eat()
