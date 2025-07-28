# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
# https://es.wikipedia.org/wiki/Código_morse.

alfabeto_morse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "ch": "----",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "ñ": "--.--",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "/": "-..-.",
        '"': ".-..-.",
    }
    
morse_text = {v : k for k, v in alfabeto_morse.items()}

def is_morse(text):
    for char in text:
        if char not in ".- ":
            return False
    return True

def translate(texto):
    palabras = [] #defino la variable antes de cualqier if, para que si o si se inicialice
    
    if is_morse(texto):
        print("Codigo morse detectado, iniciando proceso de traduccion...")
        
        #variables temporales necesarias
        frase_traducida = []
        palabras = texto.split("  ")
        
        for palabra in palabras:
            letras =  palabra.split()
            palabra_traducida = ""
            
            for letra in letras:
                if letra in morse_text:
                    letra_traducida = morse_text.get(letra)
                    
                palabra_traducida += letra_traducida  
                
            frase_traducida.append(palabra_traducida)
            
        print(" ".join(frase_traducida))  
        
    elif not is_morse(texto):
        print("Codico ASCII detectado, inicicando proceso de traduccion...")
        
        frase_traducida = []
        palabras = texto.lower().split()
        
        for palabra in palabras:
            palabra_traducida = ""
            
            for letra in palabra:
                if letra in alfabeto_morse:
                    letra_traducida = alfabeto_morse.get(letra)
                
                palabra_traducida += letra_traducida + " "
            
            frase_traducida.append(palabra_traducida)
                
        print("  ".join(frase_traducida))

    else:
        print("error, mensaje vacio o  mal codificado")


#INICIO PROGRAMA
testcase = input('Ingrese texto (normal o en codigo morse) para su traduccion segun corresponda: \n')
translate(testcase)