from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


class Staff(Weapon):
    def attack(self):
        return "Боец использует магический посох."


class Fighter:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def fight(self, monster):
        if self.weapon:
            print(self.weapon.attack())
            print(monster.defeat(self.weapon))
        else:
            print("Боец не вооружен!")


class Monster(ABC):
    @abstractmethod
    def defeat(self, weapon):
        pass


class Goblin(Monster):
    def defeat(self, weapon):
        return "Гоблин побежден!"


class Dragon(Monster):
    def defeat(self, weapon):
        return "Дракон побежден магическими способностями оружия!"


# Пример использования
fighter = Fighter("Герой")
goblin = Goblin()
dragon = Dragon()

# Боец выбирает меч и сражается с гоблином
fighter.changeWeapon(Sword())
fighter.fight(goblin)

# Боец выбирает посох и сражается с драконом
fighter.changeWeapon(Staff())
fighter.fight(dragon)
