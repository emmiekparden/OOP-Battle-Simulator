class Hero:
<<<<<<< Updated upstream
    """The hero blueprint will be implemented later in the project."""
=======
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 100

    def attack(self):
        return random.randint(1, self.attack_power)


    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        if self.health <= 0:
            self.health = 0
         


    def is_alive(self):
          return self.health > 0


    
>>>>>>> Stashed changes

    pass
