# DuckMapper

A tiny library to help you to convert classes to DTO and vice versa.

# Usage
### Using the default function
```python
class testClass():
    def __init__(self):
        self.id = None
        self.gender =None
        self.github = None
        self.name = None
        self.password = None
        self.phone_number = None

```
```python
class testDTO:
    def __init__(self):
        self.name = None
        self.github = None
        self.telephone = None
```
```python
x = testClass()
x.name = "Lucas"
x.phone_number = 99999999
x.github = "https://github.com/lucascz37"
result = convertTo(source=x, target=testDTO, default=10)
```
obs: fields not mapped will receive the value passed on the default param

### using decorator
With the same two classes created before with decorator you can specify fields that dont have the same name. My suggestion it's that you can create a class that have functions with the decorator that convert all your project's DTO to classes and the other way around.

```python
@mapBy(fields={"telephone": "phone_number"})
def convertTestClasstoTestDTO():
    pass


teste = convertTestClasstoTestDTO(source=x, target=testDTO, default=100)
```
obs: the fields dict should be like this: {"target_field1": "source_field1", "target_field2": "source_field2"...}