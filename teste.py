import characters.player, items.consumables_items, characters.hero

# characters.player.classAssassin.inventory.add_item('ITEM 1', qtd=2)

# characters.CharacterclassAssassin.inventory.show_inventory()

player = characters.player.player('Junin', 5, 2, 20)

player.inventory.add_item(items.consumables_items.healing_potion,qtd=3)

player.inventory.show_inventory()

print(player.name)