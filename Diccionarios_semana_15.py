# Crear el diccionario `informacion_personal` con datos ficticios
informacion_personal = {
    "nombre": "Juan Carlos Garcia Medrano",
    "edad": 45,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero"
}

# Modificar el valor asociado a la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor que represente el cargo en la profesión
informacion_personal["cargo"] = "Talento Humano"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0983456899"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario resultante
print(informacion_personal)
