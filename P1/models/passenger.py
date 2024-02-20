class Passenger:

    def __init__(self, name, travel_card):
        self.name = name
        self.travel_card = travel_card

        self.relations = []

    def __str__(self) -> str:
        return self.name
    
    def print_name(self) -> None:
        print('Пассажир:', self.__str__())

    def print_attributes(self) -> None:
        print('Пассажир')
        print('-----', end='\n\n')
        print('Имя:', self.name)
        print('Проездной:', self.travel_card)