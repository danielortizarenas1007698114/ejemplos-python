#datos necesarios
salario_minimo = 828116
aux_transporte = 97032


class Empleado():
    def __init__(self):
        self.codigo = input("ingrese codigo: ")
        self.nombres = input("ingrese nombres: ")
        self.apellidos = input("ingrese apellidos: ")
        self.salario_base = float(input("ingrese salario base: "))

    def calcular_retencion(self):
        retencion = self.salario_base * 0.10
        return retencion

    def mostrar_nombre_completo(self):
        return self.nombres+" "+self.apellidos 
    
    def calcular_salario_neto(self):
        if self.salario_base <= salario_minimo:
            return self.salario_base + aux_transporte
        else:
            return self.salario_base

#main
emp = Empleado()

print("-----------------")
print(emp.codigo)
print(emp.nombres)
print(emp.apellidos)
print(emp.salario_base)
print("-----------------")

print("-----------------")
print(emp.calcular_retencion())
print(emp.mostrar_nombre_completo())
print(emp.calcular_salario_neto())
print("-----------------")

