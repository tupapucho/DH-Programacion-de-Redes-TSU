''''
Nombre: Antonio Uribe Ramirez 
Asignatura: Pogramacion en Redes 
descripcion del problema: Dentro del script crear un diccionario vacío llamado asignatura donde la clave sea el
nombre de la asignatura y su valor un arreglo vacío.
Iterar por cada clave del diccionario y de acuerdo al número de unidades temáticas crear
una lista de tus calificaciones hasta el momento.
Crear una función que tome como argumento un valor y despliegue una línea de asteriscos
de acuerdo a la calificación. 
'''

asignaturas ={}

asignaturas['Ingles'] = [7, 8]
asignaturas['Programación de Redes'] = [3, 8]
asignaturas['Probalidad'] = [7, 8]
asignaturas['Sociocultural'] = [6, 8]
asignaturas['Redes Wan'] = [5, 8]
asignaturas['conexiones electrica'] = [7, 8]
asignaturas['administacion de servidores'] = [7, 8]

def barra(calificacion):
    print('*' * calificacion)

def histograma(nomb_asignatura, calif):
    print(nomb_asignatura + " histograma")
    for calif in calif:
        barra(calif)

for asignatura, calif in asignaturas.items():
    histograma(asignatura, calif)



