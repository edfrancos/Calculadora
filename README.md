# Calculadora
interfaz grafica creada con el modulo de python pyqt5

Creador: Edwin Franco Sánchez

curso: programación de computadores

Para que el programa funcione debe instalar el modulo de python Pyqt5, esto lo hara desde el simbolo de sistema en windows
con el comado: pip install PyQt5

El script calculadora.py tiene el codigo de todo lo que implica graficos, todo esto infuncional.

El script Funciones_calculadora.py es el encargado de poner a funcionar cada uno de los elementos de la calculadora, junto con cada
una de las operaciones que realiza

El script Iconos.py almacena todos los datos de almacenamiento de imagenes en formato png, esto para que el script interfaz presente ciertas caracteristicas
como los iconos de los botones

En el siguiente link: https://drive.google.com/drive/folders/1lF3uphLzl5kiW5epyTJtMrDbsZq8xUJi?usp=sharing 
encontrara alojado un archivo llamado "Calculadora_Edwin_Franco.exe" el cual es un ejecutable descargable de
la calculadora, adicionalmente encontrara un video de la calculadora funcionando.

Vitacora:
--Se reporta crasheo del ejectubale cuando se ejecutan funciones de un boton, esto posiblemente debido a un error en la creacion 
del archivo.exe que deriva de un error en la ejecucion de la libreria PyInstall, por ello hasta no solucionar dicho problema el
ejecutable no sera 100% funcional, por ello se denomina al ejecutable inicial, "Calculadora_Edwin_Franco_alfa_0.1.exe" .

--Despues de realizr debug a los scripts que conforman el progragrama se logro solucionar un problema relacionado con el crasheo del mismo, generando la segunda version de la beta del programa "Calculadora_Edwin_Franco_alfa_0.2.exe", un cambio adicional para la segunda version de la betha fue la implementacion de un icono (cal_1.ico) que se enseña en la vista previa del ejecutable. Adicionalmente, se agrego en el repositorio un video con una pequeña y breve vista previa de la ejecucion del programa llamada "Version_prueba_alfa 0.2.mp4"  
--Se reporta un nuevo crasheo que ocurre siempre que se finaliza la ejecucion de los objetos pertenecientes a la clase QMesaggeBox, este se solucionara en versiones alfa posteriores del programa.
