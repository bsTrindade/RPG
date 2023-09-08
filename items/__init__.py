from narrator import narrate

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

    def set_quantity(self, qtd):
        self.qtd = qtd

    def get_quantity(self):
        return self.qtd

class Inventory():

    def __init__(self, player_name, capacity):
        self.capacity = capacity
        self.itens = list()
        self.itens.append('CANCEL')
        self.name = player_name

    def add_item(self, item, qtd = 1):
        if len(self.itens) < self.capacity:

            if item.stackable == True and item not in self.itens:
                
                self.itens.append(item)
                if qtd != 1:
                    item.qtd = qtd

            elif item.stackable == True and item in self.itens:
                
                n = 0

                for i in self.itens:

                    if n > 0:

                        if item.name == self.itens[n].name:

                            self.itens[n].qtd += qtd
                            
                    n += 1

            else:
                
                self.itens.append(item)

            narrate(f'{qtd}x {item.name} was added to inventory.', blink=True)

        else:
            narrate(f'Inventory is full. {item.name} was discarted.', blink=True)

    def remove_item(self, item):
        self.itens.remove(item)

    # USE THE CHOSEN ITEM IF POSSIBLE
    def use_item(self, item):
        
        if item.stackable == True:
            if item.qtd > 1:
                item.qtd -= 1
            else:
                self.remove_item(item)
            print(f'Used {item.name}.\n')
            
        else:
            print(f'{item.name} cannot be used.')
            self.show_inventory(use_item=True)

    #OPEN THE INVENTORY TO SEE WHAT'S IN THERE
    def show_inventory(self, use_item = False):
        print(f"\033[1;7m{self.name.upper()}'S INVENTORY:\033[m")
        inventory_itens = self.itens
        n = 0
        for i in inventory_itens:
            if n > 0:
                print(f'|{n}| {inventory_itens[n].name} x{inventory_itens[n].qtd}')
            n += 1
        print('\n|0| Cancel')
        if use_item == True:
            
            try:
                selected_item = int(input('Select item to use: '))

                if selected_item in range(len(inventory_itens)):

                    if selected_item == 0:
                        return selected_item
                    else:
                        self.use_item(inventory_itens[selected_item])

                elif selected_item != int:
                    print('Invalid item, entry must be a number!')                              
                    self.show_inventory(use_item=True)
                else:
                    print('The item does not exist.')
                    self.show_inventory(use_item=True)
            except:
                print('Invalid item, entry must be a number!')                              
                self.show_inventory(use_item=True)
            
    def check_if_inventory_is_not_empty(self):
        return len(self.itens) > 1

        # item = int(input('Select item to use: '))
        # return item

if __name__ == "__main__":

    player_inventory = inventory('Dudu', 5)
    
    low_healing_potion = consumables('Low Healing Potion', 'Potion with low healing properties. Heals 5 HP.', 2)
    healing_potion = consumables('Regular Healing Potion', 'Potion with healing properties. Heals 15 HP.', 10)
    superior_healing_potion = consumables('Superior Healing Potion', 'Potion with great healing properties. Heals 50 HP.', 30)

    player_inventory.add_item(low_healing_potion, 2)
    player_inventory.add_item(healing_potion)

    player_inventory.show_inventory(use_item=True)
    player_inventory.show_inventory()