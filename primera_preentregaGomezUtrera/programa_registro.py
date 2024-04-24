import json

# Función para registrar usuarios
def registrar_usuario(usuarios):
    
    # Solicita el nombre de usuario y la contraseña
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    # Verifica si el nombre de usuario ya existe
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado. Intente con otro nombre.")
    else:
        # Agrega el usuario y la contraseña al diccionario
        usuarios[nombre_usuario] = contraseña
        print("Usuario registrado exitosamente.")

        # Guarda la información en un archivo JSON
        with open('usuarios.json', 'w') as archivo:
            json.dump(usuarios, archivo)

# Función para mostrar la información de los usuarios
def mostrar_informacion(usuarios):
    print("\nInformación de los usuarios registrados:")
    for usuario in usuarios:
        print(f"Usuario: {usuario}")

# Función para iniciar sesión
def login_usuario(usuarios):
    # Solicita el nombre de usuario y la contraseña
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verifica si el nombre de usuario existe y la contraseña coincide
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Función principal que ejecuta las funciones
def main():
    
    # Carga la información de usuarios desde el archivo JSON (si existe)
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        
        # Si el archivo no existe, inicializa un diccionario vacío
        usuarios = {}

    # Bucle principal del programa
    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Mostrar información")
        print("3. Iniciar sesión")
        print("4. Salir")

        # Solicita una opción al usuario
        opcion = input("Elija una opción (1-4): ")

        # Ejecuta la opción elegida
        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            mostrar_informacion(usuarios)
        elif opcion == '3':
            login_usuario(usuarios)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecuta la función principal y al mismo tiempo permite que pueda ser importado desde otro archivo.
if __name__ == "__main__":
    main()

