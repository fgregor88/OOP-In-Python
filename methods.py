#! python3
from helper import *

# Methods
print_section_title("Methods")

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(f"The speed of soldier_one is {soldier_one.get_speed()}")
