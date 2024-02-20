class BusStop:

    def __init__(self, name) -> None:
        self.name = name
        
        self.relations = []

    def __str__(self) -> str:
        return self.name

    def print_name(self) -> None:
        print('Остановка:', self.__str__())

    def print_attributes(self) -> None:
        print('Остановка')
        print('-----', end='\n\n')
        print('Наименование:', self.name)