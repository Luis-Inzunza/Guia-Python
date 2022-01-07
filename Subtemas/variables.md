## Variables
Se refiere al nombre simbolico hacia un dato, elemento o funcion.
```python
a= "Me llamo Luis "
b= " y tengo 18 años"

print (a + b)
```
En este caso nos imprimiria "Me llamo Luis y tengo 18 años".
```python
a= 5 + 7

print (a)
```
En este otro caso nos imprimiria el resultado de la operacion, que seria 12.
___

* Definir variables en una sola linea

    Se puede definir en una sola linea las variables de la sigueinte forma.
    ```python

    edad,nombre,genero = 18, "Luis", "hombre"

    ```
    Muy util para ahorrar espacio.
    ___

* Phyton como `lenguaje dinamico`

Nos referimos a esto como un lengueje que puede cambiar su tipo de variable sin nesesidad de definirlo con anterioridad.
```python
Nombre= "Luis"
Nombre= 18
Nombre= None
```
Como se observa, le damos diferente valor a la variable sin nisiquiera definir si sera de texto, entero, etc.
___

* `Case sensitive`

    Se refiere al caso de tener variables muy similares. Como el hecho de tener 2 variables iguales pero una empieza con mayuscula y la otra no.
    ```python
    Nombre= "Luis"
    nombre= "Luis"
    NombrE= "Luis"
    ```
    Todos estos son variables diferentes, ten cuidado como reescribes una variable, muy seguido se comenten estos errores.
    ___
* Convenciones(`conventiones`)

    Se refiere a la forma de escribir la variables de nombre largo, tienen diferentes nombres y cada quien tiene su gusto a como escribirlos.
    ```python
    book_name= "I robot" #Snake case
    bookName= "I robot" #Camel case
    BookName= "I robot" #Pascal case

    PI= 3.1416 #Usualmente se usa una variable de puras mayusculas para la interpetacion de una constante

    ```
    Es importante el uso adecuado de las variables para una mejor lectura del codigo.