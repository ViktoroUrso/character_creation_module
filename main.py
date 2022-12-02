from random import randint


def attack(char_name, char_class):
    demage = ''
    if char_class == 'warrior':
        demage = 5 + randint(3, 5)
    if char_class == 'mage':
        demage = 5 + randint(5, 10)
    if char_class == 'healer':
        demage = 5 + randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {demage}')


def defence(char_name, char_class):
    block = ''
    if char_class == 'warrior':
        block = 10 + randint(5, 10)
    if char_class == 'mage':
        block = 10 + randint(-2, 2)
    if char_class == 'healer':
        block = 10 + randint(2, 5)
    return (f'{char_name} блокировал {block} урона')


def special(char_name, char_class):
    skill = ''
    if char_class == 'warrior':
        skill = '«Выносливость 105»'
    if char_class == 'mage':
        skill = '«Атака 45»'
    if char_class == 'healer':
        skill = '«Защита 40»'
        return (f'{char_name} применил специальное умение {skill}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,')
    print('defence — чтобы блокировать атаку противника')
    print('или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть:')
        print('Воитель — warrior, Маг — mage, Лекарь — healer:')
        char_class = input(':')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
            print('Черпает силы из природы, веры и духов.')
        print('Нажми (Y), чтобы подтвердить выбор,')
        print('или любую другую кнопку, чтобы выбрать другого персонажа ')
        approve_choice = input(':')
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
