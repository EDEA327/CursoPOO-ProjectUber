
#! Se tiene que importar la clase desde el archivo en donde se encuentra
from car import Car
#* Entrypoint normal para cualquier programa de python 
if __name__ == "__main__":
    #* Declaración de los objetos car y car2
    car = Car()
    car.license = "MIT890"
    car.driver = "Erick"
    print(vars(car))

    car2 = Car()
    car2.license = "MIT890"
    car2.driver = "Edwin"
    print(vars(car2))

