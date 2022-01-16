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