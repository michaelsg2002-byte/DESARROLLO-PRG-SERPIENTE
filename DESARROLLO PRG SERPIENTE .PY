# UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
# AVANCE
import random 

# MODELO: Variables iniciales 
limite = 10
cuerpo = [[5, 5], [5, 4], [5, 3]]  # Lista de posiciones 
direccion = "Derecha"
comida = [3, 3]                    # Posición [X, Y] 
puntuacion = 0                     # Puntaje inicial
juego_activo = True                # Estado del juego 

# CONTROLADOR: El bucle principal del juego (Game Loop) 
while juego_activo:
    # 1. Entrada del jugador (Simulada para avanzar el código)
    nueva_entrada = input("Ingresa dirección (Arriba, Abajo, Izquierda, Derecha) o 'Salir': ")
    
    if nueva_entrada == "Salir":
        break

    # VALIDA ANTISUICIDIO: Condicionales compuestos (if, and, or)
    if (nueva_entrada == "Arriba" and direccion == "Abajo") or \
       (nueva_entrada == "Abajo" and direccion == "Arriba") or \
       (nueva_entrada == "Izquierda" and direccion == "Derecha") or \
       (nueva_entrada == "Derecha" and direccion == "Izquierda"):
        print("Movimiento inválido. No puedes ir en dirección opuesta.")
    else:
        direccion = nueva_entrad # Actualiza dirección válida 

    # 2. Mover la cabeza de la serpiente (Vectores de movimiento)
    cabeza = cuerpo[0]
    if direccion == "Arriba":
        nueva_cabeza = [cabeza[0], cabeza[1] - 1]
    elif direccion == "Abajo":
        nueva_cabeza = [cabeza[0], cabeza[1] + 1]
    elif direccion == "Izquierda":
        nueva_cabeza = [cabeza[0] - 1, cabeza[1]]
    elif direccion == "Derecha":
        nueva_cabeza = [cabeza[0] + 1, cabeza[1]]

    # 3. DETECCIÓN DE COLISIONES: Condicionales de límites y cuerpo
    if nueva_cabeza[0] < 0 or nueva_cabeza[0] >= limite or \
       nueva_cabeza[1] < 0 or nueva_cabeza[1] >= limite:
        print("¡GAME OVER! Chocaste con la pared.")
        juego_activo = False
    else:
        if nueva_cabeza in cuerpo:
            print("¡GAME OVER! Te mordiste el cuerpo.")
            juego_activo = False
        else:
            # Insertar nueva cabeza si no ha muerto
            cuerpo.insert(0, nueva_cabeza)

            # 4. PROCESAR ALIMENTACIÓN 
            if nueva_cabeza == comida:
                puntuacion = puntuacion + 10 # Incrementa puntos
                print(f"¡Comiste! Puntuación: {puntuacion}")
                
                # Bucle 'while' para generar nueva comida aleatoria libre
                ocupado = True
                while ocupado:
                    comida = [random.randint(0, limite - 1), random.randint(0, limite - 1)]
                    if comida not in cuerpo:
                        ocupado = False
            else:
                cuerpo.pop() # Elimina la cola para mantener el tamaño si no come 

    # VISTA: Mostrar estado actual en consola 
    print(f"Posición de la serpiente: {cuerpo}")
    print(f"Posición de la comida: {comida}\n")

print(f"Programa finalizado. Puntuación obtenida: {puntuacion}") 
