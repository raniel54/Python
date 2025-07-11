class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string")
        self._name = value
            
pessoa = Person("Raniel", 15)
print(vars(pessoa))