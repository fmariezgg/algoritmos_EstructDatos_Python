#Sentencias if-else anidadas
usuario = input("USUARIO: ")
usuario = usuario.upper()

if usuario == "Docente":
    print("BIENVENIDO: DOCENTE")
    password = input("Contraseña: ".upper())
    if password.upper() == "ABC123.":
        print("Usted es un usuario valido")
    else:
         print("Contraseña invalida")
else:
    print("Usuario invalido")