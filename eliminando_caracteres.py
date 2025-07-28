#  Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2):
#  - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#  - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.


def eliminar_caracteres(str1: str, str2 : str) -> tuple[str, str]:
    print("Comparando strings y eliminando caracteres...")
    out1: str = ""
    out2: str = ""
    
    for char in str1:
        if char not in str2:
            out1 += char
    
    for char in str2:
        if char not in str1:
            out2  += char
        
    return out1, out2


string1: str = input("Ingrese una cadena de caracteres cualquiera: ")
string2: str = input("Ingrese otra cadena de caracteres cualquiera: ")

out1: str
out2: str

out1, out2 = eliminar_caracteres(string1, string2)
print(f"Cadena 1: {out1} \nCadena 2: {out2}")