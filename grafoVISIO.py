from graphviz import Digraph

# Crear diagrama de actividades en UML (borrador)
dot = Digraph("Lavadora", format="png")
dot.attr(rankdir="TB", size="8")

# Nodos de inicio y fin
dot.node("Inicio", shape="circle", label="Inicio", style="filled", fillcolor="black", fontcolor="white")
dot.node("Fin", shape="doublecircle", label="Fin", style="filled", fillcolor="black", fontcolor="white")

# Acciones principales
dot.node("Sel", "Selección de programa\n(Usuario)", shape="rectangle")
dot.node("Proc", "Unidad de procesamiento\nrecibe datos", shape="rectangle")
dot.node("Params", "Procesar parámetros de operación", shape="rectangle")
dot.node("Act", "Enviar órdenes a actuadores:\n- Motor inverter\n- Válvulas de entrada\n- Bomba de drenaje\n- Resistencia calefacción", shape="rectangle")

# Sensado
dot.node("Sens", "Unidad de sensado mide:\n- Peso carga\n- Nivel de agua\n- Temperatura", shape="rectangle")

# Decisión de seguridad
dot.node("Decision", "¿Condiciones de riesgo?", shape="diamond")
dot.node("Safe", "Continuar ciclo normal", shape="rectangle")
dot.node("Stop", "Unidad de control de seguridad:\n- Detiene ciclo\n- Emite alerta\n- Señal a sistema de seguridad", shape="rectangle")

# Conexiones principales
dot.edge("Inicio", "Sel")
dot.edge("Sel", "Proc")
dot.edge("Proc", "Params")
dot.edge("Params", "Act")
dot.edge("Sens", "Proc", label="Datos")
dot.edge("Act", "Decision")
dot.edge("Decision", "Safe", label="No")
dot.edge("Decision", "Stop", label="Sí")
dot.edge("Safe", "Fin")
dot.edge("Stop", "Fin")

# Bucle de sensado
dot.edge("Safe", "Sens", style="dashed", label="Ciclo")

output_path = "/mnt/data/diagrama_lavadora"
dot.render(output_path)

output_path + ".png"
view = True