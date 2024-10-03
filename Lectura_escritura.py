# Escritura de archivo de texto
# Crear un nuevo archivo llamado my_notes.txt y escribir notas personales en él
with open('my_notes.txt', 'w') as file:  # Abrir el archivo en modo escritura
    file.write("Nota 1: Recuerda comprar frutas.\n")  # Escribir la primera nota
    file.write("Nota 2: Terminar el proyecto de Python.\n")  # Escribir la segunda nota
    file.write("Nota 3: Hacer ejercicio diariamente.\n")  # Escribir la tercera nota

# Lectura de archivo de texto
# Abrir el archivo my_notes.txt y leer su contenido línea por línea
with open('my_notes.txt', 'r') as file:  # Abrir el archivo en modo lectura
    for line in file:  # Leer cada línea del archivo
        print(line.strip())  # Mostrar la línea en consola, eliminando espacios en blanco

# El archivo se cierra automáticamente al salir del bloque 'with'
