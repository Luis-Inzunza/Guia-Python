# Se requiere determinar el tiempo que tarda una persona en llegar 
# de una ciudad a otra en bicicleta, considerando que lleva una velocidad constante.

distancia = input("¿Cuanto es la distancia de tu ciudad a la otra que gustas ir? anotalo en km ")

velocidad = input("¿Cuanta es la velocidad constante que piensas ir? anotalo en km/h ")

tiempo = float(distancia) / float(velocidad) 

punto = 0 
indice= 0

while str(punto) != ".":
      indice = indice + 1
      punto= str(tiempo)[indice]
      decimal = str(tiempo)[indice + 1]
 
#print(tiempo)
#print(punto)
#print(indice + 1)
#print(str(tiempo)[indice + 1])

#if int(decimal) == 4:
    #print("yes")
#else:
    #print("nop")

if int(decimal) == 2:

    minutos = 6
    print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 3:

    minutos = 13
    print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 4:

      minutos = 20
      print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 5:

     minutos = 26
     print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 6:

      minutos = 33
      print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 7:

     minutos = 40
     print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 8:

     minutos = 46
     print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")

if int(decimal) == 9:

      minutos = 53
      print("Llegaras aprximadamente en " + str(int(tiempo)) + " horas y " + str(minutos) + " minutos")


