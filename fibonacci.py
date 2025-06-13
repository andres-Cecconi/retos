# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores. 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci():
    serie = [0, 1] #arrancamos la serie con los dos primeros numeros, que ya lo sabemos por defecto, siempre arranca en 0 y 1.
    
    for _ in range (48):#recorremos un for 48 veces para agregar 48 numeros a nuestra seria que ya tiene 2
        suma = serie[-1] + serie[-2] #sumamos los dos ultimos numeros de la lista
        serie.append(suma) #agregamos la suma a la lista
    
    return serie #devolvemos la serie con los 48 numeros que queriamos

print(fibonacci())#imprimimos la serie llamando a la funcion
    