stuff = { 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger':2, 'arrow': 12}
DragonLoot = ['gold coin', 'torch','gold coin', 'dragon scale','arrow']

def displayInventory(inventory):
    print('Inventory: ')
    for k,v in inventory.items():
        print(f'{v} {k}')
       
    print(f'Total_items: {sum(inventory.values())}')

def add_item(inventory,item):
    for i in item:
        inventory.setdefault(i,0)
        inventory[i] += 1

print(add_item(stuff,DragonLoot))
print(displayInventory(stuff))