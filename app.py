password = input("ingrese una contraseña: ")

Mayuscula = False
Numero = False
Especial = False

for caracter in password :
    if caracter >= "A" and caracter <= "Z":
        Mayuscula = True
    
    if caracter >= "0" and caracter <= "9":
        Numero = True
    
    if not ((caracter >= "A" and caracter <= "Z") or 
            (caracter >= "a" and caracter <= "z") or 
            (caracter >= "0" and caracter <= "9")):
        Especial = True


if len(password) >= 8 and Mayuscula and Numero and Especial :
    print ("La contraseña es valida")

else :
    print ("Debe tener 8 caracteres, 1 mayuscula, 1 numero y 1 caracter especial")