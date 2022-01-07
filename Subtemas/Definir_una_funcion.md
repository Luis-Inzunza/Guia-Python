## Definir una funcion

Funciones que puedes crear para hacer el codigo de una forma mas limpia.

```python
def hello(name="persona"):
    print ("hello " + name)

hello("Luis") #En esta funcion diria "hello Luis"
hello() #Al no tener valor para name, se usara la definida en la funcion, esto entonces diria "hello persona".
```