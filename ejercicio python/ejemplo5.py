
n1 = int(input("ingrese numero: "))
n2 = int(input("ingrese numero: "))

 
operacion = int(input("digite 1 para sumar 2 para restar 3 para multiplicar 4 para dividir: "))


if operacion == 1:
    resultado = n1 + n2
elif operacion == 2:
    resultado = n1 - n2
elif operacion == 3:
    resultado = n1 * n2
elif operacion == 4:
    resultado = n1 / n2
else:
    print("escpja alguna de las opciones disponibles")

print("el resultado es: ",resultado)
    
