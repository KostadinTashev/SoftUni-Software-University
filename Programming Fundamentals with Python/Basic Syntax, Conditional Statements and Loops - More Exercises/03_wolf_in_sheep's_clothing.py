animal = input()
animal_list = animal.split(', ')
animal_list.reverse()
for idx, animal in enumerate(animal_list):
    if animal == 'wolf' and idx == 0:
        print('Please go away and stop eating my sheep')
    elif animal == 'wolf':
        print(f'Oi! Sheep number {idx}! You are about to be eaten by a wolf!')
