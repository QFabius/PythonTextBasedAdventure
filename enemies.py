## Define master Enemy() class
class Enemy:
    # Constructor
    def __init__(self, name, description, health, damage, armor=0, reward=None):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
        self.armor = armor
        self.reward = reward

    def __str__(self):
        return "{NAME}:\n\t{DESCRIPTION}".format(NAME=self.name, DESCRIPTION=self.description)
    
    def is_alive(self):
        return self.health > 0