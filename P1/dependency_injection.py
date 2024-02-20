from models.bus_stop import BusStop
from models.bus import Bus
from models.cass import Cass
from models.conductor import Conductor
from models.depot import Depot
from models.driver import Driver
from models.mechanic import Mechanic
from models.passenger import Passenger
from models.track import Track
from models.travel_card import TravelCard

objects = [
    bus_stop1 := BusStop('Угловка'),
    bus_stop2 := BusStop('Окуловка'),

    conductor1 := Conductor('Зина', 60, 50),
    conductor2 := Conductor('Галина', 62, 100),

    depot1 := Depot('Депо Угловки', 15),
    depot2 := Depot('Депо Окуловки', 15),

    driver1 := Driver('Руслан', 45, 20),
    driver2 := Driver('Къурбан-КIажи', 50, 30),

    travel_card1 := TravelCard('123456', '29.02.2024', 67),
    travel_card2 := TravelCard('654321', '29.02.2024', 63),
    travel_card3 := TravelCard('162534', '29.02.2024', 35),

    passenger1 := Passenger('Иван', travel_card1),
    passenger2 := Passenger('Николай', travel_card2),
    passenger3 := Passenger('Анна', travel_card3),

    track := Track(2, [bus_stop1, bus_stop2], False),

    bus1 := Bus('1ААА11 78', '2023', driver1, conductor1, [passenger1, passenger2], track, [depot1, depot2]),
    bus2 := Bus('2БББ22 78', '2021', driver2, conductor2, [passenger3], track, [depot1, depot2]),

    mechanic1 := Mechanic('Петрович', 72, '1 разряд'),
    mechanic2 := Mechanic('Михалыч', 65, '2 разряд'),
    cass := Cass(10000, 1200)
]

bus_stop1.relations = [track]
bus_stop2.relations = [track]
bus1.relations = [passenger1, passenger2, driver1, conductor1, track, depot1, depot2]
bus2.relations = [passenger3, driver2, conductor2, track, depot1, depot2]
cass.relations = [travel_card1, travel_card2, travel_card3]
conductor1.relations = [bus1]
conductor2.relations = [bus2]
depot1.relations = [bus1, bus2, mechanic1]
depot2.relations = [bus1, bus2, mechanic2]
driver1.relations = [bus1]
driver2.relations = [bus2]
mechanic1.relations = [depot1]
mechanic2.relations = [depot2]
passenger1.relations = [bus1, travel_card1]
passenger2.relations = [bus1, travel_card2]
passenger3.relations = [bus2, travel_card3]
track.relations = [bus1, bus2, bus_stop1, bus_stop2]
travel_card1.relations = [passenger1, cass]
travel_card2.relations = [passenger2, cass]
travel_card3.relations = [passenger3, cass]