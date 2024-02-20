class Bus:

    def __init__(self, state_number, release_year, driver, conductor, passengers, track, depots) -> None:
        self.number = state_number
        self.release_year = release_year
        self.driver = driver
        self.conductor = conductor
        self.passengers = passengers
        self.track = track
        self.depots = depots

        self.relations = []

    def __str__(self) -> str:
        return self.number

    def print_name(self) -> None:
        print('Автобус:', self.__str__())

    def print_attributes(self) -> None:
        print('Автобус')
        print('-----', end='\n\n')
        print('Госномер:', self.number)
        print('Год выпуска:', self.release_year)
        print('Водитель:', self.driver)
        print('Кондуктор:', self.conductor)
        print('Пассажиры:', ', '.join(map(str, self.passengers)))
        print('Маршрут:', self.track)
        print('Возможные депо:', ', '.join(map(str, self.depots)))