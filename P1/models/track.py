class Track:

    def __init__(self, length, bus_stops, has_road_works) -> None:
        self.length = length
        self.bus_stops = bus_stops
        self.has_road_works = has_road_works

        self.relations = []

    def __str__(self) -> str:
        return f'{self.bus_stops[0]} - {self.bus_stops[-1]}'
    
    def print_name(self) -> None:
        print('Маршрут:', self.__str__())

    def print_attributes(self) -> None:
        print('Маршрут')
        print('-----', end='\n\n')
        print('Протяжённость:', self.length, 'км')
        print('Остановки:', ', '.join(map(str, self.bus_stops)))
        print('Ремонтные работы:', 'да' if self.has_road_works else 'нет')