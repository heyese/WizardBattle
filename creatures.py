import random


class Creature:

    def __init__(self, power=None):
        self.name = self.__class__.__name__
        self.power = power if power else random.randint(1, 10)
        self.description = random.choice(['slimy', 'terrifying', 'terrible', 'snotty',
                                          'stinky', 'purple', 'slobbering', 'bimbling',
                                          'preposterous', 'daft', 'evil', 'murderous'])

    def __str__(self):
        return self.__class__.__name__

    def attack(self):
        return self.power * random.randint(1, 10)

class Wizard(Creature):

    def __init__(self, power=None):
        super().__init__(power)
        self.sex = random.choice(['male', 'female'])

    def level(self):
        if self.power < 4:
            level = 'newbie'
        elif self.power < 8:
            level = 'experienced'
        else:
            level = 'veteran'
        return level

class Dragon(Creature):

    def __init__(self, power=None):
        super().__init__(power)
        self.power *= 2


class Bat(Creature):

    def __init__(self, power=None):
        super().__init__(power)
        self.power //= 2

