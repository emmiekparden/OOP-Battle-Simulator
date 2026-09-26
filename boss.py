from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""
    def introduce(self, name):
        print(f"a mysterious power appears to be present in the battle.. {self.name} ")
        

    def __init__(self, name):
        super().__init__(name, health=300, attackPower=10)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} releashes a catastrophic punch!")
        return damage + bonus_damage