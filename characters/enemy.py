import random
from items import consumables_items
from characters import Character

class Enemy(Character):

    def __init__(self, name="", level=1):
        name = self.__class__.__name__
        
        super().__init__(name, level)

    @classmethod
    def encounter(cls, level):
        enemies = cls.__subclasses__()
        enemy_cls = random.choice(enemies)
        return enemy_cls(level=level)
    
    def drop_items(self):
        drop_items_list_range = len(self.enemy_loot_pool)
        item_droped = self.enemy_loot_pool[random.randint(0, drop_items_list_range - 1)]
        item_droped.set_quantity(random.randint(1,2))
        return item_droped
        

class Rat(Enemy):
    base_attack = 1
    base_defense = 2
    base_hp = 6
    enemy_loot_pool = [consumables_items.low_healing_potion]

class Bat(Enemy):
    base_attack = 2
    base_defense = 2
    base_hp = 8
    enemy_loot_pool = [consumables_items.low_healing_potion]

class Slime(Enemy):
    base_attack = 1
    base_defense = 6
    base_hp = 10
    DEFENSE_MULTIPLIER_CONST = 0.2
    enemy_loot_pool = [consumables_items.low_healing_potion]

class Skeleton(Enemy):
    base_attack = 3
    base_defense = 1
    base_hp = 10
    enemy_loot_pool = [consumables_items.low_healing_potion, consumables_items.healing_potion]

class Orc(Enemy):
    base_attack = 3
    base_defense = 3
    base_hp = 15
    enemy_loot_pool = [consumables_items.low_healing_potion, consumables_items.healing_potion, consumables_items.superior_healing_potion]

class Troll(Enemy):
    base_attack = 5
    base_defense = 3
    base_hp = 10
    enemy_loot_pool = [consumables_items.healing_potion, consumables_items.superior_healing_potion]

if __name__ == '__main__':
    rat = Rat()
    print(len(rat.enemy_loot_pool))