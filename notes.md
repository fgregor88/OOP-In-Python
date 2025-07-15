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

## Methods

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

# Encapsulation

## Private data members
Private data members are directly accessible with the "." operator.

They are denoted with "__" at the beginning of the property name.

Python doesn't enforce the "__" rule, it's just a naming convention. You can still get around this. Getter method.

```python
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina # <- private
        self.__intelligence = intelligence # <- private
        self.name = name
        self.health = 100 * stamina
        self.mana = 10 * intelligence

    # getter method for private __stamina field
    def get_stamina():
        return self.__stamina
```

# Abstraction

Abstraction helps us handle complexity by hiding uneecessary details.

## Abstraction vs Encapsulation

- Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed (publis).
- Encapsulation is about hiding internal state. It focuses on tucking away the implementation details (private).

## Example

```python
import random

attack_damage = random.randrange(5)
```

# Inheritance

A class can inheric members and methods from another class. We say that they are in an perent - child relationship.
The subclass (child class) inherites everything ... EVERYTHING ... So don't use ingeritance if you don't want this.

Basic example of class inheritance. Animal is the parent class, Dog is the child class. We can use the Animals constructor to assign the inherited members. "super()" method is used to access parents members and methods.

```python
class Animal:
    def __init__(self, alive):
        self.alive = alive

class Dog(Animal):
    def __init__(self, alive, breed):
        super().__init__(alive)
	self.breed = breed
```

# Polymorphism

Polymorphism in programming is the ability to present the same interface (function or method signature) for many different underlying forms (data types).

- "poly" means "many"
- "morph" means "to change" or "form"

A classic example is a Shape class that Rectangle, Circle and Triangle can inherit from. Each has different underlying data:
- The circle needs its center point coordinates and radius
- The rectangle needs two coordinates for the top left and bottom right corners
- The triangle needs coordinates for the corners

## Examples

```python
def draw_shape(self)

shapes = [Circle(5,5,10), Rectangle(1,3,5,6)]
for shape in shapes:
    print(shape.draw_space())
```

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
	return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
	return self.health
```	


