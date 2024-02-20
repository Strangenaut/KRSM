class Driver:

    def __init__(self, name, age, work_experience) -> None:
        self.name = name
        self.age = age
        self.work_experience = work_experience

        self.relations = []

    def __str__(self) -> str:
        return self.name
    
    def print_name(self) -> None:
        print('Водитель:', self.__str__())

    def print_attributes(self) -> None:
        print('Водитель')
        print('-----', end='\n\n')
        print('Имя:', self.name)
        print('Возраст:', self.age)
        print('Стаж работы:', self.work_experience)