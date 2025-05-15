import requests
import json
import os


DEBUG=True


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    admin = True if DEBUG else False
    salir = False
    id = 0
    while not salir:
        clear_console()
        opc = int(input('\t0. Salir\n\t1. Iniciar session\n\t2. Prueba\n\t3. Crear Usuario\n\t4. Eliminar usuario\n\t5. Cerrar session\n\tOpcion: '))
        
        if opc == 0:
            clear_console()
            print('Saliendo de la app')
            salir = True
        elif opc == 1:
            clear_console()
            print('Iniciar sesión')
            nombre = input('Ingresa el nombre del usuario: ')
            password = input('Ingresa la contraseña: ')
            response = requests.post(
                url + '/session/',
                json={"nombre": nombre, "password": password}
            )
            
            clear_console()
            if response.status_code == 200:
                data = response.json()
                id=data['id']
                print(f"Inicio de sesión exitoso\n\t* ID: {data['id']}\n\t* Nombre: {data['nombre']}")
            else:
                print("Error:", response.text)
            
            input("\nPresiona Enter para continuar...")

        elif opc == 2 and id !=0:
            clear_console()
            print('URL de prueba')
            response = requests.get(url + f'/user/{id}')
            
            if response.status_code == 200:
                data = response.json()
                print(f' * id: {data["id"]}\n * nombre: {data["nombre"]}')
            else:
                print(f"Error: {response.text}")
            
            input("\nPresiona Enter para continuar...")

        elif opc == 3 and admin:
            clear_console()
            print('Crear Usuario')
            nombre = input('Ingresa el nombre del usuario: ')
            password = input('Ingresa la contraseña: ')
            response = requests.post(
                url + '/create/',
                json={"nombre": nombre,"password": password}
            )
            
            clear_console()
            if response.status_code == 201:
                data = response.json()
                print(f"Usuario creado:\nID: {data['id']}\nNombre: {data['nombre']}")
            else:
                print("Error:", response.text)
            
            input("\nPresiona Enter para continuar...")
        elif opc == 4:
            clear_console()
            print('Eliminar usuario')
            user_id = input('Ingresa el ID del usuario a eliminar: ')

            response = requests.delete(url + f'/eliminar/{user_id}')

            clear_console()
            if response.status_code == 200:
                data = response.json()
                print(data["msg"])
            elif response.status_code == 404:
                print("Error: El usuario no existe.")
            else:
                print("Error:", response.text)

            input("\nPresiona Enter para continuar...")
        
        elif opc == 5:
            clear_console()
            print('Cerrar session')
            
            id=0

            input("\nPresiona Enter para continuar...")