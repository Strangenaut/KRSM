class Cass:

    def __init__(self, travel_cards_count, travel_card_price) -> None:
        self.travel_cards_count = travel_cards_count
        self.travel_card_price = travel_card_price

        self.relations = []

    def __str__(self) -> str:
        return ''
    
    def print_name(self) -> None:
        print('Касса')

    def print_attributes(self) -> None:
        print('Касса')
        print('-----', end='\n\n')
        print('Количество доступных проездных:', self.travel_cards_count)
        print('Стоимость покупки проездного:', self.travel_card_price, 'деревянных')