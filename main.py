#5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#- как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения значений этого атрибута
# нужно использовать методы get  и set

#5.2 Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий


class Person:
    some_num = 123
    def __init__(self, name, lastname, placeofbirth, yearofbirth):
        self.name = name                                        # <-- атрибуты класса
        self.lastname = lastname
        self.placeofbirth = placeofbirth
        self.yearofbirth = yearofbirth
    def printInfo(self, n):
        for i in range(n):
            print(f'Name = {self.name},Last Name = {self.lastname},POB = {self.placeofbirth}')
    def get_age(self, current_year):
        return current_year - self.yearofbirth

p1 = Person('I.S.', 'Bach', 'Germany', 1685)
p2 = Person('W.A.', 'Mozart', 'Austria', 1756)
p3 = Person('Sergey','Rachmaninoff', 'Russia', 1873)


p3.printInfo(1)

#Person.printInfo(p1)