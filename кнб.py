a = input()
b = input()
 
if a == b:
    print('ничья')
elif a == 'камень' and b == 'ножницы':
    print('Тимур')
elif a == 'ножницы' and b == 'бумага':
    print('Тимур')
elif a == 'бумага' and b == 'камень':
    print('Тимур')
elif a == 'камень' and b == 'бумага':
    print('Руслан')
elif a == 'бумага' and b == 'ножницы':
    print('Руслан')
elif a == 'ножницы' and b == 'камень':
    print('Руслан')
elif a == 'ящерица' and b == 'камень':
    print('Руслан')
elif a == 'камень' and b == 'ящерица':
    print('Тимур')
elif a == 'Спок' and b == 'камень':
    print('Тимур')
elif a == 'камень' and b == 'Спок':
    print('Руслан')
elif a == 'ящерица' and b == 'Спок':
    print('Тимур')
elif a == 'Спок' and b == 'ящерица':
    print('Руслан')
elif a == 'Спок' and b == 'ножницы':
    print('Тимур')
elif a == 'ножницы' and b == 'Спок':
    print('Руслан')
elif a == 'ножницы' and b == 'ящерица':
    print('Тимур')
elif a == 'ящерица' and b == 'ножницы':
    print('Руслан')
elif a == 'ящерица' and b == 'бумага':
    print('Тимур')
elif a == 'бумага' and b == 'ящерица':
    print('Руслан')