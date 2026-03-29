"""
4 Pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism
"""
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

enemy = Enemy()
enemy.type_of_enemy = 'Zombie'
print(f'{enemy.type_of_enemy} has health of {enemy.health_points} and damage of {enemy.attack_damage}')
