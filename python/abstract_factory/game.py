class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact(self, obstacle):
        print("{} frog  found{} and took the action {}".format(self, obstacle, obstacle.action()))

class Bug:
    def __str__(self):
        return 'bug'

    def action(self):
        return 'eat'

class Wizzard:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def interact(self, obstacle):
        print("{} wizzard found {} and took the action {}".format(self, obstacle, obstacle.action()))

class Which:
    def __str__(self):
        return 'which'

    def action(self):
        return 'killed'


class FrogWorld:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '----FROG WORLD---'
    
    def make_character(self):
        return Frog(self.name)

    def make_obstacle(self):
        return Bug()

class WizzardWorld:
    def __init__(self, name):
        self.name = name

    def __str__(self):
            return '------ Wizard World -------'
    
    def make_character(self):
        return Wizzard(self.name)

    def make_obstacle(self):
        return Which()



class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact(self.obstacle)


def validate_age(name):
    try:
        age = input("welcome {}! how old are you".format(name))
        age = int(age)
    except ValueError as ve:
        print("age {} is invalid, please try again")
        return False, age
    return True, age


def main():
    name = input("hello what's your name ?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age <= 13 else WizzardWorld
    env = GameEnvironment(game(name))
    env.play()

if __name__ == '__main__':
    main()
    
