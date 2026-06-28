```mermaid
graph TD
    %% Definición de Estilos Globales
    classDef caja fill:#000,stroke:#fff,stroke-width:2px,stroke-dasharray: 5 5,color:#fff;
    classDef texto fill:none,stroke:none,color:#fff,font-family:monospace;

    %% Bloque CONTROLADOR
    C["<b>CONTROLADOR</b><br><ul style='text-align:left;'><li>Gestiona el Game Loop (while juego_activo).</li><li>Captura entradas de teclado (input).</li><li>Aplica las reglas lógicas y vectores de movimiento.</li></ul>"]
    class C caja;

    %% Texto intermedio de las flechas
    T1["Modifica / Actualiza<br>los datos"]
    T2["Envía datos de<br>coordenadas limpias"]
    class T1,T2 texto;

    %% Bloque MODELO
    M["<b>MODELO</b><br><ul style='text-align:left;'><li>cuerpo (Lista)</li><li>comida (Coordenadas)</li><li>puntuacion (Entero)</li><li>juego_act. (Bool)</li></ul>"]
    class M caja;

    %% Bloque VISTA
    V["<b>VISTA</b><br><ul style='text-align:left;'><li>print(cuerpo)</li><li>print(comida)</li><li>print(Puntuación)</li></ul>"]
    class V caja;

    %% Conexiones y flujo
    C --> T1 --> M
    C --> T2 --> V
