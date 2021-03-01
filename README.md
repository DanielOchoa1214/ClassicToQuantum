# Libreria de simulacion de lo clasico a lo cuantico 


## Resumen
Esta libreria contiene las siguientes operaciones sobre sistemas deterministicos, probabilisticos y cuanticos

* Funcion que determina el estado de un vector segun un sistema (Tanto deterministico como probabilistico) y unos clicks dados, ademas del vector de estado inicial.
* Funcion que simula el problema de las probabilidades de una bala en terminar en un blanco (Problema de la pagina 86 del libro Quantum Computing for Computer Scientist)
* Funcion que silula el estado de un sistema cuantico.
* Funcion que imprime las probabilidades de un vector dado de estar en un nodo del sistema, en una grafica de barras.

## Comenzando
Para poder correr correctamente la libreria es importante fijarse que se descargen los siguientes archivos:

* deterministicSystems.pu
* suportFunctions.py
* testDeterministicSystems.py

Es importante que se encuentren todos estos archivos pues los primeros 2 juntos completan la libreria que se pidio y el ultimo, es el archivo de puebas de la libreria

## Instalación
1. Para instalar python solo debe ir al sitio web oficial de python.
2. Debe ir a la sección de "Downloads" y descargar la última versión que le recomienda. 
3. Una vez que lo tenga descargado, ejecuta el archivo y le da a instalar.
4. Para Pycharm debe hacer lo mismo, ir al sitio web y buscar la opción "descargar".
5. Ejecuta el archivo y acepta términos y condiciones, para despues darle en instalar.
6. Al tener descargado python, ejecuta Pycharm y abre la carpeta de la libreria de los sistemas.
7. Verá que en un panel de la derecha de Pycharm tendrá todos los archivos de la carpeta que se usaran.
8. Si abre el archivo deterministicSystems.py, junto con suportFunctions.py podrá ver todas las operaciones que contiene la librería.
9. Luego si abre el archivo testDeterministicSystems podra ver las puebas que se hicieron para validar las funciones

## Ejecutar el test
Para ejecutar el test solo debe abrir el archivo testDeterministicSystems.py y ejecuta el modulo presionando "ctrl + shift + f10" si esta en Windows, si esta en mac solo debe presionar "shift + control + r".

## Prerequisitos
* Python 3.8
* Un editor de texto 

## Como correr las pruebas
Para hacer las prubas correr el archivo llamado testDeterministicStatesTests.py 

## Hecho con
* Python - Lenguaje de Programación
* Pycharm - IDE
* Git - Control de versiones
* GitHub - Aloja las versiones de Git

## Notas
* Ademas se le agrego un modulo a la libreria en el cual esta las funciones de apoyo (suportFunctions.py), en este caso solo es una la la cual es npToList, la cual lo unico que hace es transformar el objeto np.array() (El cual representa, los estados en los sistemas) a una lista nativa de python para que la funcion que grafica las graficas de barras sirviera correctamente.
* Al momento de hacer las pruebas con unittest surgia un error y era que debido a que python maneja solo decimales cuando se veia forzado a usar raices los valores de estas eran redondeados, por lo que al comparar valores con los reales estos daban un valor muy cercano, pero no igual, por lo que, unittest decia que los resultados no eran iguales. 
* Ademas de que por la misma razon que en lo anterior cuando se trabaja con raizes, por estas mismas aproximaciones, al operar, python llegaba a un resultado por ejemplo 2e-17 lo cual es un valor muy cercano a 0, que si se usara el valor completo de las raizes se llegaria a este.; pero que tecnicamente esta correcto, ya que la difereccia es despreciable.
* En esta libreria los vectores se consideran como listas de listas, para facilitar los calculos al momento de determinar el estado del sistema. (Multiplicar las matrices)

## Autor 
Daniel Sebastian Ochoa Urrego 

## Agradecimientos
Gracias a todos lo que utilicen esta libreria, ojala les sirva <3

