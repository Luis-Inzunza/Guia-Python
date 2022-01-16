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