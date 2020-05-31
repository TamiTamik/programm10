from function1 import create, remove, showMenu, show, change

n = 1

while n > 0:
    showMenu()
    n = int(input('uildliin dugaar oruulna uu: '))
    if n == 1:
        show()
    elif n == 2:
        create()
    elif n == 3:
        remove()
    elif n == 4:
        change()
    else:
        print('ta programmas garlaa...')
        break