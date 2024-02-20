class TravelCard:

    def __init__(self, serial_number, expiration_date, travels_left) -> None:
        self.serial_number = serial_number
        self.expiration_date = expiration_date
        self.travels_left = travels_left

        self.relations = []

    def __str__(self) -> str:
        return self.serial_number

    def print_name(self) -> None:
        print('Проездной:', self.__str__())

    def print_attributes(self) -> None:
        print('Проездной')
        print('-----', end='\n\n')
        print('Серийный номер:', self.serial_number)
        print('Дата истечения срока действия:', self.expiration_date)
        print('Количество оставшихся поездок:', self.travels_left)