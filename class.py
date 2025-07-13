#! python3
from helper import *

print("Hello, this is just a bunch of random code found in the course")

# Class
print_section_title("Class")

class Soldier:
    armor = 10
    attack = 20

soldier_one = Soldier()
soldier_two = Soldier()

print(f"The armor of soldier_one is: {soldier_one.armor}")
print(f"The attack of soldier_tow is: {soldier_two.attack}")

