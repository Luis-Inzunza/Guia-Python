distancia = input("¿Cuanto es la distancia de tu ciudad a la otra que gustas ir? anotalo en km ")

velocidad = input("¿Cuanta es la velocidad constante que piensas ir? anotalo en km/h ")

tiempo = float(distancia) / float(velocidad) 

punto = 0 
indice= 0
while str(punto) != ".":
      indice = indice + 1
      punto= str(tiempo)[indice]
      
print("hello")
