peso = int(input("ingrese peso"))
estatura = int(input("ingrese estatura"))

imc = peso/(estatura*estatura)

if imc < 18.5:
    print("bajo peso")
    print("tomese la sopita mijo")
elif imc >= 18.5 and imc <= 24.9:
    print("normal")
elif imc >= 25 and imc <= 29.9:
    print("sobrepeso")
    print("haz dieta")
elif imc >= 30 and imc <= 34.9:
    print("obesidad 1")
    print("estas gordo bro")
elif imc >= 35 and imc <= 39.9:
    print("obesidad 2")
    print("haga ejercicio")
elif imc >= 40 and imc <= 49.9:
    print("obesidad 3")
    print("ve al gym porfa")
elif imc >= 50:
    print("obesidad 4")
    print("busca ayuda")

S
