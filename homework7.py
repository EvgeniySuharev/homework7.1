my_dict = {'Женя': 1988, 'Настя': 1992, 'Миша': 1989, 'Соня': 2014}
print('Dict:', my_dict)
print('Existing value:', my_dict['Женя'])
print('Not existing value:', my_dict.get(1))
my_dict.update({'Вася': 1900, 'Петя': 1965})
print('Deleted value:', my_dict.pop('Женя'))
print('Modified dict:', my_dict)
print()
my_set = {1, 'one', (1, 'one'), 'uno', (1, 'one'), 'uno', 1.1, 'one'}
print('Set:', my_set)
my_set.update({'один', 'ichi'})
my_set.remove(1.1)
print('Modified set:', my_set)
