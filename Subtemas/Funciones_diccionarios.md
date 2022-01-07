## Funciones `dictionaries/diccionario`

```python

product= {
    "name" : "Book",
    "cantidad" : 3,      # Ejemplo de un diccionario
    "precio" : 4.99,
}

persona= {
    "nombre" : "Luis",     # Ejemplo de un diccionario
    "apellido" : "Cruz",
}


print(persona.keys()) #Nos mostrara los datos con los que cuenta el diccionario (los del lado izquierdo de los 2 puntos).

print(persona.items())  #Nos da los valores completos del diccionario, divididos por tuplas.

persona.clean()

#Ejemplo de una lista de productos

productos = [

    {"nombre": "libro", "precio" : 5.99},
    {"nombre": "pluma", "precio" : 1.99},  #Recordar el coma despues de un diccionario
    {"nombre": "hojas", "precio" : 0.99}
    
    ]

```