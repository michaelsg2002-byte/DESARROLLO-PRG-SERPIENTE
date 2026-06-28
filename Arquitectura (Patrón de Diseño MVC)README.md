```mermaid
graph TD
    %% Definición de los componentes principales con saltos de línea HTML
    C["CONTROLADOR
    • Gestiona el Game Loop (while juego_activo).
    • Captura entradas de teclado (input).
    • Aplica las reglas lógicas y vectores de movimiento."]

    M["MODELO
    • cuerpo (Lista)
    • comida (Coordenadas)
    • puntuacion (Entero)
    • juego_act. (Bool)"]

    V["VISTA
    • print(cuerpo)
    • print(comida)
    • print(Puntuación)"]

    %% Conexiones con el flujo correcto de arquitectura MVC
    C -->|1. Modifica / Actualiza los datos| M
    M -->|2. Envía datos actualizados para renderizar| V
    C -.->|3. Dispara ciclo de dibujado / Render| V
