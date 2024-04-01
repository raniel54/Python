class Employee:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.__salario = salario #Metodo para deixar atributo privado __
    
    def show(self):
        print(f"Nome {self.nome} - Salário {self.__salario}")
        
    # Metodo para buscar dados
    
    def get_salary(self):
        return self.__salario
    # Metodo para Modificar atributo privado
    
    def set_salario(self, salario):
        self.__salario = salario
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("sicrano", 5000)
fulano.nome = "Fulano 2"
fulano.show()
sicrano.show()
fulano.__salario = 40000
fulano.show()
fulano.set_salario(10000)
fulano.show()
    