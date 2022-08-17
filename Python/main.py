
#! Se tiene que importar la clase desde el archivo en donde se encuentra
from car import Car
from account import Account
#* Entrypoint normal para cualquier programa de python 
if __name__ == "__main__":
    #* Declaración del objeto car
    '''
    Recuerda que car recibe la placa y el conductor
    Account recibe nombre y documento del objeto sea usuario o..
    Sea conductor en este caso debido a la composicion de car
    Estamos hablando del conductor.
    Por ultimo el objeto car se crea con su respectiva placa y conductor.
    '''
    car = Car("AMZ456",Account("Erick","5465643"))
    print(vars(car))
    print(vars(car.driver))


