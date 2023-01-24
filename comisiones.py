nombre = input("Dime tu nombre: ")
venta = input("¿Cuanto fue tu venta?: ")
venta = int(venta)

comisiones = venta*0.13
comisiones = round(comisiones)

print(f"Hola {nombre}, tus comisiones son de ${comisiones}\n¡FELICIDADES!")