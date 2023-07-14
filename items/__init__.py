

class itens():

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.stackable = False

class weapons(itens):

    def __init__(self, name, description, value, attack, acc):
        super().__init__(name, description, value)

        self.attack = attack
        self.acc = acc

class armors(itens):

    def __init__(self, name, description, value, defense, eva):
        super().__init__(name, description, value)

        self.defense = defense
        self.eva = eva

class consumables(itens):

    def __init__(self, name, description, value, qtd=1):
        super().__init__(name, description, value)

        self.stackable = True
        self.qtd = qtd

class inventory():

    def __init__(self, capacity):
        self.capacity = capacity
        self.itens = []

    def add_item(self, item, qtd = 1):
        if len(self.itens) < self.capacity:

            if item.stackable == True and item not in self.itens:
                print('CAIU 1')
                self.itens.append(item)
                if qtd != 1:
                    item.qtd = qtd

            elif item.stackable == True and item in self.itens:
                print('CAIU 2')
                n = 0
                for i in self.itens:
                    if item.name == self.itens[n].name:
                        self.itens[n].qtd += qtd
                    n += 1

            else:
                print('CAIU 3')
                self.itens.append(item)

            print(f'{qtd}x {item.name} was added to inventory.')

        else:
            print(f'Inventory is full. {item.name} was discarted.')

    def remove_item(self, item):
        self.itens.remove(item)

    def use_item(self, item):
        if item.qtd > 1:
            item.qtd -= 1
        else:
            self.remove_item(item)

    def show_inventory(self):
        print('INVENTORY:')
        n = 0
        for i in self.itens:
            print(f'{self.itens[n].name} x{self.itens[n].qtd}')
            n += 1

if __name__ == "__main__":

    player_inventory = inventory(5)
    
    low_healing_potion = consumables('Low Healing Potion', 'Potion with low healing properties. Heals 5 HP.', 2)
    healing_potion = consumables('Regular Healing Potion', 'Potion with healing properties. Heals 15 HP.', 10)
    superior_healing_potion = consumables('Superior Healing Potion', 'Potion with great healing properties. Heals 50 HP.', 30)

    player_inventory.add_item(low_healing_potion, 2)
    player_inventory.add_item(healing_potion)

    player_inventory.show_inventory()

    player_inventory.use_item(low_healing_potion)

    player_inventory.show_inventory()