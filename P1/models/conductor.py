class Conductor:

    def __init__(self, name, age, tickets_count) -> None:
        self.name = name
        self.age = age
        self.tickets_count = tickets_count

        self.relations = []

    def __str__(self) -> str:
        return self.name
    
    def print_name(self) -> None:
        print('Кондуктор:', self.__str__())

    def print_attributes(self) -> None:
        print('Кондуктор')
        print('-----', end='\n\n')
        print('Имя:', self.name)
        print('Возраст:', self.age)
        print('Количество оставшихся билетов:', self.tickets_count)