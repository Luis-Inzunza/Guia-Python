## `if/else`
```python

x= 20

if x < 30:    #ejemplo de if
    print ("x es menor a 30")
else:
    print ("x es mayor a 30")

color = "rojo"

if color == "verde":
    print( "El color es verde")

elif color == "rojo":    #elif es volver a poner de nuevo una condicion, en total tenemos 3 caminos diferentes dependiendo la variable.
    print( "El color es rojo")
else:
    print ("El colo no se identifica")
```
___

## `For/ a partir de..`
```python

#Se quiere imprimir todo lo de la lista comida
comida = ["manzana", "zanahoria", "lechuga", "pera"]

print(comida[0])
print(comida[1])      #que pasa si queremos agregar otro mas? se agregara otro print..
print(comida[2])
print(comida[3])

#Esto seria muy laborioso hacerlo todas las veces que se registra un nuevo alimento
#Por lo tanto usaremos el siclo for

for comidas in comida: #esto es mas efectivo
    print(comida)

```