class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100

    def slashing_blow(self):
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'

    def sharpen(self):
        self.strength = 100
        return f'Оружие "{self.name}" заточено.'


class Sword(MeleeWeapon):

    def slashing_blow(self):
        self.strength -= 5
        return f'Мечом {self.name} был нанесен рубящий удар.'


class Axe(MeleeWeapon):
    ...


brodex = Axe('Верный')
xiphos = Sword('Разящий')

print(xiphos.slashing_blow())
print(brodex.slashing_blow())
print(xiphos.strength)
print(brodex.strength)
