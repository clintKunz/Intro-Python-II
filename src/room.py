# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return str(f'{self.name}, {self.description}')

    def add_item(self, item):
        self.items.append(item)
        print(f'{self.name} now has a {item.name}')

    def remove_item(self, item):
        self.items.remove(item)
        print(f'{self.name} had a {item.name} removed from it')

    def show_items(self, item):
        if len(self.items) > 0:
            print('Here are the items in this room:')
            for i in self.items:
                print(f'{i.name}')