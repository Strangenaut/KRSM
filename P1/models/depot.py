class Depot:

    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

        self.relations = []

    def __str__(self) -> str:
        return self.name
    
    def print_name(self) -> None:
        print('Депо:', self.__str__())

    def print_attributes(self) -> None:
        print('Депо')
        print('-----', end='\n\n')
        print('Наименование:', self.name)
        print('Вместимость:', self.capacity)