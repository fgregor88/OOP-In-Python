# Object Oriented Programming

## Clean Code

Only Uncle Bob knows ...

## Dry

Don't repeat yourself.

# Class

A class is a new custom type, but instead of being a built-in type, classes are custom types that you define.

## Object

A object is an instance of a class. For example Opel Insiagnia is an instance of an car. A tomato is an instance of a vegetable (it's not a fruid I don't care what people say ...)

## Examples

```python
class Archer:
    health = 40
    arrows = 10

legolas = Archer()
bard = Archer()

print(legolas.health)
print(bard.arrows)
```

# Methods

A method is a function that's directly tied to a class and has access to its properties.
The first parameter to a method is the instance of the class itself ("self").

## Self
Methods first parameter is the instance of the class and by convention this is called "self".

## Examples

```python
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# print "3"
```

## Constructors

A constructor is a specific method for initilizing a instance of a class.
It's defined with "__init__" method.

```python
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
	self.armor = armor
	sefl.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 2, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "2"
print(soldier_one.num_weapons)
# prints "10)
```

## Class Variables vs. Instance Variables

Class variables are usually a bad idea. Initialize properties through the constructor.

```python
class Wall:
    height = 10 # <- this is a class variables, it is shared between all instances of the Wall class
```

```python
class Wall:
    __init__(self, height):
        self.height = height # <- instance varibles, every object has it's own value
```
