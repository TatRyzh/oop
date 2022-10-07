#5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#- как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения значений этого атрибута
# нужно использовать методы get  и set

#5.2 Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий


class Animal:
    #some_num = 123              # атрибуты класса (статические атрибуты), все обекты класса имеют доступ

    def __init__(self, name):
        self.name = name                                        # <-- атрибуты об'ектов класса

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    # переопределим конструктор для собаки - персональный
    def __init__(self, name, breed):
        #Animal.__init__(self, name, breed)
        super().__init__(name)          # указание на родительский конструктор
        self.breed = breed

        print(f"A dog {self.name} of breed {self.breed} is created")
    def bark(self):
        print(f'{self.name} is barking')


class Cat(Animal):
    def meow(self):
        print(f'{self.name} is meowing')

class Frog(Animal):

    def eat(self):
        print(f'{self.name} is eating')


d=Dog ('Druzhok', 'Terrier')
c = Cat ('Murka')
f= Frog ('Kwakwa')

d.bark()
d.breed         # почему метод breed без скобок?
d.eat()
c.meow()
c.eat()
f.eat()



