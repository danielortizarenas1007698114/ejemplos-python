print ("hola mundo")

edad = int(input("ingrese su edad: "))
genero = input("ingrese su genero H para hombre y M para mujer ")

if edad >= 18:    
    if genero in 'Hh':    
        print ("señor ")    
    elif genero in 'Mm':    
        print ("señora ")        
    else:
        print("error 404")        
if edad <= 18:
    if genero in 'Hh':        
        print ("niño")
    elif genero in 'Mm':        
         print ("niña")        
    else:
        print("error 404")
