print("------------------------")
print("---COSTO DE UNA LLAMDA--")
print("------------------------")

#INPUT
duracion_llamada = int(input("digite la duración de la llamada: "))


#PROCESSING
if duracion_llamada > 3:
  costo_llamada = 300 + 50*(duracion_llamada - 3)
else:
  costo_llamada = 300

#OUTPUT
print("el costo de la llamada es" + str(costo_llamada))
