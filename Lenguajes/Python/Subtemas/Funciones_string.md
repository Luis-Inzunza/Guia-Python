## Funciones `string`

```python
my_string = "hello world"

print(my_string.upper()) #pone todo el texto en mayusculas

print(my_string.lower()) #pone todo el texto en minusculas

print(my_string.swapcase()) #Te alterna entre mayusculas y minuscula

print(my_string.capitalize()) #Vuelve la primera letra en mayuscula

print(my_string.replace("hello", "bye")) #Sustitulle parte del texto por otro, haciendo uso del sintaxis mostrado. En este caso cambiamos el hello por bye.

print(my_string.replace("hello", "bye").upper()) #Aqui juntamos 2 funciones, primero remplazamos y despues colocamos todo a mayusculas

print(my_string.count("l")) #Nos contara cuantas veces se utilizo cierto caracter o conjunto de caracteres, en este caso la l se uso 3 veces en "hello world". devuelve valores enteros.

print(my_string.startswith("hola")) #buscamos si inicia de la forma que mencionamos, en este caso no es asi asi que nos devolvera falso. devuelve valores booleanos.

print(my_string.endswith("world")) #buscamos si termina de la forma que mencionamos, en este caso si es, entonces nos devolvera verdadero. devuelve valores booleanos.

print(my_string.split()) #Separa tu valor de string en varios strings dependiendo sobre que quieres que se separen (esta por defecto que se separe por espacios), especificando entre los parentecis y comillas dentro de ellas. Te termina dando una lista de strings.

print(my_string.find("_")) #el valor que le des entre parentecis buscara en que lugar queda en todo el string contando a partir de 0. Ejemplo: find "o" de "hello", nos devolveria el valor 4.

print(len(my_string)) # cuenta los caracteres totales que tiene el string a partir del 1.

print(my_string.index("")) #Devuelve el lugar en donde se ubica en cunato a caracteres. empezando a contar desde el 0

print(my_string[]) #con esto, al poner un numero en el corchete, nos dara el caractes ubicado en ese espaciado. si usas numeros negativos, lo leera desde el final al inicio
```