# Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas. Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

palabra1: str = input("Ingrese una palabra: ")
palabra2: str = input("Ingrese una segunda palabra: ")

#OPCION 1
# def es_anagrama(a, b):
#     """
#     En esta opcion utilizamos la funcion sorted para ordenar alfabeticamente cada str y comparar.
#     """
#     if a == b:
#         return False
#     elif len(a) != len(b):
#         return False
#     elif sorted(a) == sorted(b):
#         return True



#OPCION 2
def es_anagrama(a, b):
    """
    En esta version, creamos dos diccionarios para cada str si para las primeras validaciones, y luego comparamos diccioarios, que son desordenados, por lo cual no es problema el orden de las letras. Si diccionario a y b tienen los mismos chars, y la cantidad tb, son iguales, por ende son anagramas
    """
    if a == b:
        return False
    elif len(a) != len(b):
        return False
    else:
        dict_a = {}
        dict_b = {}
        for char in a:
            if char in dict_a:
                dict_a[char] += 1
            else:
                dict_a[char] = 1
        
        for char in b:
            if char in dict_b:
                dict_b[char] += 1
            else:
                dict_b[char] = 1
        
        return dict_a == dict_b

print(es_anagrama(palabra1, palabra2))