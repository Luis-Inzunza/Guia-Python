<!--Se encierra entre tildes para escribir codigo sin afectar el markdown, usa Alt+96 para crear la tilde-->

<!--Usamos triple tilde para poner bloques de codigo, puedes agregar el tipo de lenguaje para que se remarque a ese tipo de lenguaje-->

# Guia de Python
Aqui se escribiran funciones basicas para su completo uso, mejor dichas como palabras reservadas para pyhton.
___
## Tipos de datos
Aqui se mencionaran todas las forma que podemos ingresar datos de entrada. 

* String/Cadena/texto
Se usa para identificar texto y para identificarlo se escribe entre comillas o de otras formas, como se muestra a continuacion. 
<!-- Se hace con comilla simple y triple comilla simple tambien-->
```python
"hola mundo"
"""hola mundo"""
```

 * Concadenacion 
    
    Se usa para juntar 2 strings
    ```python
    "bye" + "world"
    ```
    En este caso, nos daria "byeworld" sin espacio, ya que no dejamos en ninguno de los 2 strings.

___
* Numero Entero (`integer`) y Con decimales (`float`)

Se usa para identificar numeros, pero no son nesesarios si solo se ocupa sin definirlos en variables.

```python
30 # Esto ya se lee como numero entero 
30.5 #Esto seria un numero con decimales

# de la misma forma se determina como...
int 30
float 30.5
```
___
* Booleanos (`True` y `False`)

Se usa para identificar si las condiciones propuestas se cumplen o no.

```python
True

False

```
___
* Lista/Matrices (`List`)

Se usa para agrupar diferentes valores. agrupados entre corchetes y separados por una coma.

```python
[10, 20, "hello", True, 30.4]

```
___
* Tupla/matriz sin cambios (`Tuple`)

Se usa para agrupar diferentes valores. agrupados entre parentecis y separados por una coma. Estos no pueden cambiarse.

```python
(10, 20, "hello", True, 30.4)

```
___

* Diccionario (`Dictorionies`)

Se usa para agrupar y definir valores, pero en un solo elemento. Se hace entre llaves y se define una clave "`key`" con su respectivo valor "`value`"

```python
{
    "nombre":"Luis",
    "apellido":"Cruz",
    "apodo":"Wicho"
}

```
___

* Nada (`None`)

Se usa para determinar un valor vacio.

```python

a= None
```
Esto se refiere que a tiene un valor vacio o nulo pero no es 0.
___

## `input()`

Se utiliza para pedir datos de entrada, dentro del parentecis puedes ser mas especifico o para que sera dirigido la entrada.

```python
input()

input("ingresa tu nombre")

a = input ("edad")
```
Aqui es donde el usuario colocara los datos.
___

## `Print()` 

Se usa para mostrar lo que este entre parentecis.

```python
Print ("hello word")
```
Esto nos mostrara un texto diciendo "hello word"
___

## `type()` 

Se usa para desifrar el tipo de valor que tiene entre parentecis.

```python
type("hello word")
type(100)
```
Esto nos mostrara un texto diciendo el tipo de valor que es.
___

## `# Comentrario`
Despues del # se mostrara como comentario
```python
#Este comentario sirve de ejemplo y no afecta en nada.
```
___

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
___
 
## `dir()`

Esta funcion nos dara las funciones que podemos aplicar a lo que tenga dentro del parentecis.
```python
my_string = "hello word"

print(dir(my_string))
```
En este ejemplo, nos dara todas las funciones que podemos aplicare a esta variable de texto/string.
___

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
___

## Funciones `Integer/Enteros`

```python
1 + 1 #suma
1 - 1 #resta
1 * 1 #multiplicacion
1 / 1 #Division
1 ** 1 #Elevacion
1 // 1  o  1 % 1 #modulo (devuelve la cantidad restante de una division)

#Recuerda que los valores que ingresa el usuario seran string, por lo tanto siempre debemos mencionar que tipo de dato se maneja.
```
___

## Funciones `List/matrices/arreglos`

```python

list_numeros = list((1,2,3,4)) #Ejemplo de creacion de lista

colors = ["red", "blue", "yellow"] #Ejemplo de creacion de lista

colors[1]= "green" #aqui cambiamos a uno de los valores de la lista, aqui se numeran a partir del 0. por lo tanto, el blue cambiara a green


m = list(range(1,10)) #lista con numeros del 1 al 9 (siempre un numero antes del 2do que pusimos)

print("green" in colors) #devolvera un valor de verdadero o falso si lo puesto antes de "in" est dentro de la lista

print(len(colors)) #Nos dara la longitud que tiene la lista, cunatos elementos tiene

colors.append("violet") #Se agrega un espacio mas en la lista, esta sera llenado por el string "violet". solo se uede agregar un solo elemento. si usas una list, se agregara un solo elemento como lista (en otras palabras una sublista en dicho apartado que ocupa).

colors.extend(["black", "white"]) #Se usa para agregar varios elementos a la lista, utilizando una lista dentro del parentecis de extend.

colors.insert(1,"pink") #aqui especificamos que despues del elemento 1, se agregue un espacio nuevo con el elemento que mencinamos enseguida del coma.

colors.pop() #Quita el ultimo elemento de la lista.
colors.pop(3) #Quita el elemento de dicho indice de la lista.

colors.remove("green") #Quita (remueve) el elemento especificado

colors.clean() #Limpia por completo la lista

colors.sort() #Acomoda alfabeticamente la lista (A-Z)
colors.sort(reverse= True) #acomoda alfabeticamente inverso la lista (Z-A)

colors.index("red") #obtenemos el indice del elemento mencionado.

colors.count("red") #cuantas veces se repite el elemento en la lista.


```
___

## Funciones `Tuples/Tupla/Arreglo sin cambios`

```Python
x = (1, 2, 3) #Ejemplo sencillo de tupla
y = tuple(1, 2, 3) #Exactamente lo mismo
Meses = ("Enero", "Febrero", "Marzo", "Abril", ...) #Un ejemplo mas real

z = (1,) #Esta seria la tupla de un solo elemento, si le quitamos la coma, python lo identificara como un simple entero aun estando entre parentecis.

del x #Accion para borrar variables.

#Las tupplas usan los mismos comandos que las listas, solo que los que cambian los elementos no seran aplicables.

```
___

## Funciones `Set`

Son una lista pero sin indice, no tienen un orden como tal y debemos pedirlos de una manera diferente. Se menciona los elementos dentro de las llaves {}

```python

colors = {"red", "blue", "green"} #Ejemplo de Set

#Utiliza varios comandos de lo de la listas, la diferencia es que no tiene indice y al agregar un nuevo elemento se agrega en cualquier lugar.

```