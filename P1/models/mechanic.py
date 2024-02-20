class Mechanic:

    def __init__(self, name, age, qualification) -> None:
        self.name = name 
        self.age = age 
        self.qualification = qualification

        self.relations = []

    def __str__(self) -> str:
        return self.name
    
    def print_name(self) -> None:
        print('Автомеханик:', self.__str__())

    def print_attributes(self) -> None:
        print('Автомеханик')
        print('-----', end='\n\n')
        print('Имя:', self.name)
        print('Возраст:', self.age)
        print('Квалификация:', self.qualification)