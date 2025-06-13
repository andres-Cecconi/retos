
# Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calcular_area(poligono):
    match poligono:
        case "triangulo":
            base  = int(input("ingrese la longitud de la base expresada en cm: "))
            altura = int(input("ingrese la longitud de la altura expresada en cm: "))
            area = (base*altura)/2
            return f"El área del {poligono} ingresado es de {area} cm."
    
        case "cuadrado":
            base = int(input("ingrese la longitud de uno de los lados: "))
            area= base**2
            return f"El área del {poligono} ingresado es de {area} cm."
    
        case "rectangulo":
            base  = int(input("ingrese la longitud de la base: "))
            altura = int(input("ingrese la longitud de la altura: "))
            area =  base*altura
            return f"El área del {poligono} ingresado es de {area} cm."
        case _: 
            return "Poligono no soportado"

poligono = input("Ingrese el poligono del cual quiera comprobar el área: triangulo, cuadrado o rectangulo: ").strip().lower()
print(calcular_area(poligono))