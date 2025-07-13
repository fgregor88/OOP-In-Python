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
