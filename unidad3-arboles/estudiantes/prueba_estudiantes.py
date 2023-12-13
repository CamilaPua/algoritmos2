from estudiante import Estudiante
from a_estudiantes import ArbolBinarioEstudiantes

print('-' * 17 + ' Prueba arbol vacio ' + '-' * 17)
arbol_vacio = ArbolBinarioEstudiantes('')
print('Visualización arbol:\n', arbol_vacio.verArbol())
print('Estudiantes con nota de 3:', arbol_vacio.estudiantes_con_nota(3))

print('\n' + '-' * 20 + ' Prueba arbol ' + '-' * 20)
camila = ArbolBinarioEstudiantes(Estudiante(1, 'Camila', '13/09/2003', notas=[3, 4, 5]))
jose = ArbolBinarioEstudiantes(Estudiante(2, 'Jose', '21/12/2004', notas=[2, 3, 2.5]))
andrea = ArbolBinarioEstudiantes(Estudiante(3, 'Andrea', '31/02/2005', notas=[5, 5, 5]))
carolina = ArbolBinarioEstudiantes(Estudiante(4, 'Carolina', '29/11/1997', notas=[4, 2, 3]))
juan = ArbolBinarioEstudiantes(Estudiante(5, 'Juan', '28/10/2009', notas=[1, 1, 1]))
carlos = ArbolBinarioEstudiantes(Estudiante(6, 'Carlos', '17/02/2004', notas=[3, 4, 4.2]))

camila.hijo_izquierdo = jose
camila.hijo_derecho = andrea
jose.hijo_izquierdo = carolina
carolina.hijo_izquierdo = juan
andrea.hijo_derecho = carlos

print('Visualización arbol:\n', camila.verArbol())
print('Estudiantes con una nota de 4:', camila.estudiantes_con_nota(4))

for nodo in camila.estudiantes_con_nota(4):
    print(f'Notas de {nodo}: {nodo.estudiante.notas}')

print('\n' + '-' * 12 + ' Prueba notas que nadie tiene ' + '-' * 12)
print('Estudiantes con una nota de 0:', camila.estudiantes_con_nota(0))
print('Estudiantes con una nota de -5:', camila.estudiantes_con_nota(-5))
