"""Wizard Battle game"""
import importlib
import random
import collections
import sys

import creatures as c


def main():
    # Hero wizard is initialised with randomised power.
    # List of creatures initialised, random length
    # Game loop - [d]efend, [r]un away, [l]ook at surroundings or [c]onsider stats.
    # Defeating a creature increases hero's experience
    # Wizard can be attached while running away, but has greater chance of escaping

    # Initial setup - create the wizard and creatures
    power = random.randint(1, 10)
    hero = c.Wizard(power)
    (him_her, he_she, his_her) = ('him', 'he', 'his') if hero.sex == 'male' else ('her', 'she', 'her')

    creatures = collections.defaultdict(list)
    num_creatures = random.randint(3, 10)
    for i in range(num_creatures):
        # Following line instantiates one of the subclasses of creature at random
        creature = random.choice(c.Creature.__subclasses__())()
        creatures[creature.name].append(creature)

    print('Our hero is a {} wizard of power {}'.format(hero.level(), hero.power))
    print('{} faces a scary horde of enemies, comprising:'.format(he_she.title()))
    print_creatures(creatures)
    print('Can you guide {} through these perilous encounters to safety ...\n'.format(him_her))

    enemy = None
    while True:
        creature_type = random.choice(list(creatures.keys()))
        if not enemy:
            enemy = random.choice(creatures[creature_type])
        choice = input('A {} {} is attacking!\nShould our hero [f]ight back, [r]un away, [l]ook around'
                       ' or carefully [c]onsider {} chances? : '.format(
                        enemy.description,
                        enemy.name,
                        his_her
                        ))

        if choice == 'f':
            hero_attack, enemy_attack = hero.attack(), enemy.attack()
            print('The {} rolls a {}!\nOur hero rolls a {}!!'.format(
                enemy.name, enemy_attack, hero_attack))
            if enemy_attack > hero_attack:
                print('Sadly, our hero has been defeated ...')
                sys.exit()
            else:
                print('Our hero is victorious!!  One less {} to deal with.'.format(enemy.name))
                creatures[enemy.name].remove(enemy)
                if len(creatures[enemy.name]) == 0:
                    del(creatures[enemy.name])
                hero.power += random.randint(1, enemy.power)
                print('{} power has now increased to {}.'.format(his_her.title(), hero.power))
                enemy = None

        elif choice == 'l':
            print('Our hero takes a swift look around.  {} sees:'.format(he_she.title()))
            print_creatures(creatures)

        elif choice == 'c':
            print('Our hero, who has power {}, senses that {} '
                  'enemy\'s power is {}'.format(hero.power, his_her, enemy.power))

        elif choice == 'r':
            hero_attack, enemy_attack = hero.attack(), enemy.attack()//2
            print('Our hero tries to make a run for it ...')
            if enemy_attack > hero_attack:
                print('... but rolls a {} compared to the {} {}s {} and is defeated.'.format(
                    hero_attack, enemy.description, enemy.name, enemy_attack
                ))
                sys.exit()
            print('... and rolls a {} compared to the {} {}\'s {} and so succeeds in escaping!'.format(
                hero_attack, enemy.description, enemy.name, enemy_attack
            ))
            enemy = None
        print()
        if not creatures:
            print('Congratulations!  Our hero has vanquished all enemies and is now safe.')
            sys.exit()


def print_creatures(creatures):
    for creature_type in creatures:
        num_type = len(creatures[creature_type])
        s = 's' if num_type > 1 else ''
        print('{} {}{}'.format(num_type, creature_type, s))


if __name__ == '__main__':
    main()
