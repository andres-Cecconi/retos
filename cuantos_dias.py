#  Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
#  - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  - La función recibirá dos String y retornará un Int.
#  - La diferencia en días será absoluta (no importa el orden de las fechas).
#  - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

from datetime import datetime


# def es_mayor(fecha1: str, fecha2: str) -> bool:
#     f1: datetime = datetime.strptime(fecha1, "%d/%m/%Y")
#     f2: datetime = datetime.strptime(fecha2, "%d/%m/%Y")
    
#     return f1 > f2
    
def calcular_dias(fecha1: str, fecha2: str) -> int:    
    try:
        f1: datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        f2: datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        
        diferencia : int = abs((f1 - f2).days) #abs devuelve el valor absoluto, por lo que no importa que fecha es mayor, resta, y quita el signo si el resultado es negativo. Y .days extrae el numero de dias del objeto timedelta
        return diferencia
    except ValueError:
        print("Error, formato de fecha INCORRECTO")
        return -1


prueba = input("Ingrese una fecha en formato dd/mm/aaaa: ")
prueba2 = input("Ingrese otra fecha en formato dd/mm/aaaa: ")


print(calcular_dias(prueba, prueba2))
