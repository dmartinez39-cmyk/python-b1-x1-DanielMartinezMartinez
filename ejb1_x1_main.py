"""El objetivo general del ejercicio es crear una serie de funciones que nos permitan realizar operaciones 
sobre un texto.

Para este ejercicio, no se debe usar la función split de Python. En vez de ello, deberás  usar las 
siguientes funciones auxiliares que serán de gran ayuda al resolver el ejercicio. Asimismo, se pueden 
elegir crear nuevas funciones adicionales. A continuación, presentaremos una descripción de estos métodos:

* is_newline(character): Es una función que detecta el final de una oración. Deberás suponer que las frases 
están separadas por "\n" (nueva línea). Si el carácter es este símbolo, devolverá True.

* is_space(character): Es una función que detecta si un carácter es un espacio en blanco. Si el carácter es 
este símbolo, devolverá True.

* remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de una palabra o un texto. 
Este método devuelve como resultado una cadena de caracteres sin signos de puntuación.

Las funciones descritas en el apartado anterior forman parte del módulo denominado 'text_manager.py', por lo tanto, 
es preciso importar estas en el módulo 'ejb1_x1_main.py', el cual es el módulo principal en el que desarrollaremos 
nuestra solución. 
En este ejercicio utilizaremos  la variable "TEXT" de tipo cadena de caracteres(definida en el módulo text_manager.py), 
la cual será empleada en cada una de las siguientes funciones como parámetro. Los métodos que se solicita 
desarrollar son:

* find_largest_word(text): Un método que permite detectar la palabra más larga en un texto. Este método debe 
devolver como resultado una cadena de caracteres correspondiente a la palabra más larga. Al evaluar la palabra
no debe contener signos de puntuación. 

* is_palindrome_word(word): Es una función recursiva que nos permitirá detectar si una palabra es palíndromo. 
Un palíndromo es una palabra que se lee igual en un sentido que en otro. Por ejemplo las siguientes palabras son 
palíndromos: Ata; Aviva; Azuza; Apa; Afromorfa. Para el ejercicio, el texto se encuentra en lengua inglesa, 
por lo que no se requiere realizar ningún tipo de acción en relación con tildes o acentos. Al evaluar la palabra 
no debe contener signos de puntuación. El valor que devuelve es de tipo booleano. Si es un palíndromo devolverá 
"True", y en el caso contrario "False". 

* count_palindrome_words(text): Se trata de una función que nos permitirá enumerar las apariciones de palíndromos 
en el texto, por lo tanto, esta retorna un número entero. Para esto debemos hacer uso de la anterior 
función is_palindrome_word(word).

* find_size_largest_sentence(text, filter): Se trata de una función que permite encontrar el tamaño de la oración 
más larga cuyo valor de filtro esté en esa sentencia. Si no existe una oración que coincida con el filtro deberá 
lanzar una excepción del tipo ValueError. El valor a retornar es un número entero que representa la longitud de 
la cadena en cuestión. 
Por ejemplo: si se invoca a la función con los parámetros text = "Hola, Pepe.\n¿Cómo estás, amigo?", el parámetro
filter = "a", este debe devolver 19, ya que en la segunda oración "¿Cómo estás, amigo?", se encuentra incluido 
el valor pasado como filtro y la oración tiene una longitud de la cadena de texto más larga. 
"""
# Add your imports here
from util_package import text_manager 
from util_package.text_manager import TEXT, is_newline, is_space, remove_punctuation_marks

def find_largest_word(text):
    current_word = ""
    largest_word = ""
    for char in text:
        if is_space(char) or is_newline(char):  # Detecto el final de la palabra
            word_clean = remove_punctuation_marks(current_word)  # Limpio current_word
            if len(word_clean) > len(largest_word):  # Comparo la longitud de la palabra
                largest_word = word_clean  # Si es más grande, la guardo en largest_word
            current_word = ""
        else:
            current_word += char  # Si no se detecta final de palabra, acumulo el carácter

    # Procesamos la última palabra si es la más larga
    word_clean = remove_punctuation_marks(current_word)
    if len(word_clean) > len(largest_word):
        largest_word = word_clean
    
    return largest_word
          

def is_palindrome_word(word):
    word_clean = remove_punctuation_marks(word)  # Limpiamos la palabra
    word_lower = word_clean.lower()  # Convertimos todas las letras a minúsculas
    if len(word_lower) == 0 or len(word_lower) == 1:  # Caso base: longitud 0 o 1
        return True
    else:
        if word_lower[0] == word_lower[-1]:  # Comparamos la primera y última letra
            return is_palindrome_word(word_lower[1:-1])  # Llamada recursiva a la palabra central
        else:
            return False  # Si no son iguales, no es palíndromo
        
def count_palindrome_words(text):
    num_palindrome = 0
    current_word = ""
    
    for char in text:
        if is_space(char) or is_newline(char):  # Detecto final de palabra
            if is_palindrome_word(current_word):  # Llamamos a la función is_palindrome_word
                num_palindrome += 1  # Si devuelve True, sumamos 1 al contador
            current_word = ""
        else:
            current_word += char  # Acumulamos caracter por caracter para formar la palabra

    # Procesamos la última palabra
    if is_palindrome_word(current_word):
        num_palindrome += 1
    
    return num_palindrome

def find_size_largest_sentence(text, filter):
    current_sentence = ""
    largest_sentence = ""
    found = False

    for char in text:
        if is_newline(char):
            # Procesar oración completa
            if filter in current_sentence:  # Comprobamos que la oración contiene el filtro
                if len(current_sentence) > len(largest_sentence):  # Comparamos el tamaño de la oración con la más larga
                    largest_sentence = current_sentence  # Si es más grande, la guardamos como la más larga
                found = True  # Marcamos que se encontró el filtro
            current_sentence = ""  # Borramos la oración para comprobar la siguiente
        else:
            current_sentence += char

    # Procesar última oración si no termina con \n
    if current_sentence != "":
        if filter in current_sentence:
            if len(current_sentence) > len(largest_sentence):
                largest_sentence = current_sentence
            found = True

    if not found:  # Si found es False, no se encontró el filtro en todo el texto
        raise ValueError(f"No se encontró ninguna oración con el filtro '{filter}'")

    return len(largest_sentence)  # Devolvemos la longitud de la oración más larga con el filtro



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
try:
    print("La palabra más larga es:", find_largest_word(TEXT))
    print("'aa' es un palíndromo, su resultado es:", is_palindrome_word("aa"))
    print("'a' es un palíndromo, su resultado es:", is_palindrome_word("a"))
    print("'Ababa' es palíndromo, su resultado es:", is_palindrome_word("Ababa"))
    print("El número de palabras identificadas como palíndromos es:", count_palindrome_words(TEXT))
    print("El tamaño de la oración más larga con el filtro='a' es:", find_size_largest_sentence(TEXT, "a"))
except ValueError as e:
    print(f"El tamaño de la oración más larga con el filtro='españa' es: Error,", e)

