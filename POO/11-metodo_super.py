class fone:
    def __init__(self, brand, model_name,price) -> None:
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self) -> str:
        return f"{self._brand}{self._model_name}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")
        
class celular(fone):
    def __init__(self, brand, model_name, price, ram, memoria_interna, camera_traseira ):
        super().__init__(brand, model_name, price) #nos permite referir explicitamente à classe pai. É útil no caso de 
                                                     #herança onde queremos chamar funções de superclasse
        
        self.ram = ram
        self.memoria_interna = memoria_interna
        self.camera_traseira = camera_traseira
iphone = fone('Iphone: ', '15 Pro Max', 4500)
print(iphone)

iphone.make_a_call(62998754124)
print(f"valor do {iphone._brand}{iphone._model_name} é {iphone._price}")
print(vars(iphone))

xiomi = celular("Xiomi: ", "Poco X3", 2.100, "12GB", "128GB", "108MP")
print(xiomi)
xiomi.make_a_call(1138259874)
print(f"valor do {xiomi._brand}{xiomi._model_name} é {xiomi._price}")
print(vars(xiomi))
        

        