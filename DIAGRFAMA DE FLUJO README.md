```mermaid
graph TD
    Inicio([Inicio])
    InitVar[Inicializar variables: cuerpo, comida, limite, puntuacion, juego_activo=True]
    CheckActivo{¿juego_activo es True?}
    PuntFinal[Mostrar Puntuación Final]
    Fin([Fin del Programa])
    
    Input[Capturar nueva_entrada input]
    CheckInverso{¿Es un movimiento inverso / anti-suicidio?}
    MovInvalido[Imprimir Movimiento invalido - Mantiene direccion anterior]
    ActDir[Actualizar variable: direccion = nueva_entrada]
    
    CalcCabeza[Calcular coordenadas de nueva_cabeza segun direccion]
    CheckColision{¿nueva_cabeza fuera de limites O dentro de cuerpo?}
    GameOver[Imprimir GAME OVER - juego_activo = False]
    
    InsCabeza[Insertar nueva_cabeza en posicion cuerpo 0]
    CheckComida{¿nueva_cabeza == comida?}
    Eats[puntuacion += 10 - Generar comida aleatoria libre]
    NoEats[cuerpo.pop -> Eliminar ultimo segmento]
    Vista[Vista: Imprimir estado de cuerpo y comida en consola]

    Inicio --> InitVar
    InitVar --> CheckActivo
    
    CheckActivo -- No --> PuntFinal --> Fin
    
    CheckActivo -- Si --> Input
    Input --> CheckInverso
    
    CheckInverso -- Si --> MovInvalido --> CalcCabeza
    CheckInverso -- No --> ActDir --> CalcCabeza
    
    CalcCabeza --> CheckColision
    
    CheckColision -- Si --> GameOver
    GameOver --> CheckActivo
    
    CheckColision -- No --> InsCabeza
    InsCabeza --> CheckComida
    
    CheckComida -- Si --> Eats --> Vista
    CheckComida -- No --> NoEats --> Vista
    
    Vista --> CheckActivo
