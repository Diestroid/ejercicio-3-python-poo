import time

class Personaje:
    def __init__(self, nombre, vel_mov, vel_ataque, ataque):
        self.nombre = nombre
        self.velMov = vel_mov
        self.velAtaque = vel_ataque
        self.ataque = ataque

    def __str__(self):
        return f"Nombre: {self.nombre} Habilidades: velMov={self.velMov} velAtaque={self.velAtaque} ataque={self.ataque}"

    def __add__(self, otro):
        def fusion(primero, segundo):
            return ((primero + segundo) / 2) ** 2

        return Personaje(self.nombre + otro.nombre, fusion(self.velMov, otro.velMov), fusion(self.velAtaque, otro.velAtaque),
                         fusion(self.ataque, otro.ataque))

# Bucle principal

lista_personajes = []

while True:
    print("""
    --------------------------------------------------------------
    --------------------------------------------------------------
                        1. Crear personaje
                        2. Fusionar personajes
                        3. Alterar personajes
                        4. Mostrar personajes
                        5. Salir
    --------------------------------------------------------------
    --------------------------------------------------------------
    """)
    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        while True:
            nombre = input("\nIntroduce el nombre de  tu personaje: ").lower()
            vel_mov = int(input("Introduce la velocidad de movimiento de tu personaje: "))
            vel_ataque = int(input("Introduce la velocidad de ataque de tu personaje: "))
            ataque = int(input("Introduce el ataque: "))

            personaje_actual = Personaje(nombre, vel_mov, vel_ataque, ataque)        
            lista_personajes.append(personaje_actual)
            continuar = input("\nCrear otro personaje: ").lower()

            if continuar == "no":
                break
                
    elif seleccion == "2":
        primer_personaje = input("\nNombre del primer personaje: ").lower()
        segundo_personaje = input("Nombre del segundo personaje: ").lower()

        iterador_busqueda = 0
        for personaje in lista_personajes:
            if iterador_busqueda >= len(lista_personajes):
                break
            else:
                if personaje.nombre == primer_personaje:
                    primer_personaje_encontrado = personaje
                    iterador_busqueda += 1
                    
                elif personaje.nombre == segundo_personaje:
                    segundo_personaje_encontrado = personaje
                    iterador_busqueda += 1
                    

        resultado_personaje = primer_personaje_encontrado + segundo_personaje_encontrado
        print("El nuevo personaje es:\n")
        print(resultado_personaje)
        lista_personajes.append(resultado_personaje)
        time.sleep(5)

    elif seleccion == "3":
        personaje_alterar = input("Nombre actual del personaje a alterar: ")
 
        # buscar personaje
        for personaje in lista_personajes:
            if personaje.nombre == personaje_alterar:
                personaje_encontrado = personaje
                break

        print("""
    1. Nombre
    2. Velocidad de movimiento
    3. Velocidad de ataque
    4. Ataque
    5. Mejor no
    """)
        a_alterar = input("Quieres alterar: ")
        
        if a_alterar == "1":
            nuevo_nombre = input(f'Nuevo nombre para {personaje_encontrado.nombre}: ').lower()
            personaje_encontrado.nombre = nuevo_nombre
            print(f'Nombre cambiado a {nuevo_nombre}')
            time.sleep(5)
        
        elif a_alterar == "2":
            nueva_vel_mov = input(f'Nueva velocidad de ataque para {personaje_encontrado.nombre}: ')
            personaje_encontrado.vel_mov = nueva_vel_mov
            print(f'Velocidad de movimiento cambiada a {nueva_vel_mov}')
            time.sleep(5)

        elif a_alterar == "3":
            nueva_vel_ataque = input(f'Nueva velocidad de ataque para {personaje_encontrado.nombre}: ')
            personaje_encontrado.vel_ataque = nueva_vel_ataque
            print(f'Nueva velocidad de ataque es {nueva_vel_ataque}')
            time.sleep(5)
        
        elif a_alterar == "4":
            nuevo_ataque = input(f'Nuevo ataque para {personaje_encontrado.nombre}: ')
            personaje_encontrado.ataque = nuevo_ataque
            print(f'Ataque cambiado a {nuevo_ataque}')
            time.sleep(5)

    
    elif seleccion == "4":
        print("\nLista de personajes: \n\n")
        iterador_mostrar = 1
        for personaje in lista_personajes:
            print(f'{iterador_mostrar}. {personaje}')
            iterador_mostrar += 1
        time.sleep(5)
    
    elif seleccion == "5":
        print("Chau")
        break
            
