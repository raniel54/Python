class Employee:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.__salario = salario #Metodo para deixar atributo privado __
    
    def show(self):
        print(f"Nome {self.nome} - Salário {self.__salario}")
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("sicrano", 5000)
fulano.show()
sicrano.show()
fulano.__salario = 40000
fulano.show