# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.itemsBag = []

    def __str__(self):
        return str(f'{self.name}, {self.current_room}')
    
    def pick_up_item(self, item):
        self.itemsBag.append(item)
        print(f'{self.name} picked up a {item.name}')

    def drop_item(self, item):
        self.itemsBag.remove(item)
        print(f'{self.name} dropped a {item.name}')