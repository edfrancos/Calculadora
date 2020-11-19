import sys
import math

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from  Calculadora import*

class Funciones_calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.advertencias = QMessageBox()
        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.comboBox.currentIndexChanged.connect(self.seleccion_menu)
        self.ui.btn_regresar_cuadratica.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.btn_regresar_pendiente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.btn_regresar_primos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))

        self.ui.btn_cuadratica_solucion.clicked.connect(self.cuadratica)
        self.ui.btn_pendiente_calc.clicked.connect(self.pendiente)
        self.ui.vsd_inicio_intervalo.valueChanged.connect(self.mostrar_inicio)
        self.ui.vsd_final_intervalo.valueChanged.connect(self.mostrar_final)
        self.ui.btn_primos_inter.clicked.connect(self.primos)

    def seleccion_menu(self):
        combo = self.ui.comboBox.currentIndex()
        print(combo)
        if combo == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ecuaciones)
        elif combo ==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_pendiente)
        elif combo ==3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_primos)
    
    def mostrar_inicio(self,valor):
        self.ui.txt_inicio_intervalo.setText("Inicio intervalo: {}".format(valor))

    def mostrar_final(self,valor):
        self.ui.txt_final_intervalo_2.setText("Final intervalo: {}".format(valor))
    def primos(self):
        a_1 = self.ui.vsd_inicio_intervalo.value()
        b_1 = self.ui.vsd_final_intervalo.value()
        if a_1 < b_1:
            Cd = 0
            D = 1
            lista_primos = []
            while b_1 >= a_1:
                while a_1 >= D:
                    if a_1 % D == 0:
                        Cd += 1
                    D += 1
                if Cd == 2:
                    lista_primos.append(a_1)
                Cd = 0
                a_1 += 1
                D = 1
            self.ui.lbl_solucion_interval_primos.setText("{}".format(lista_primos))
        else:
            self.advertencias.setText("El valor inicial del intervalo es mayor que el final")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()

    def pendiente(self):
        if len(self.ui.txt_pendiente_x.text()) > 0:
            x_1 = float(self.ui.txt_pendiente_x.text())
        else:
            self.advertencias.setText("No ha ingresado la coordenada x_1")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_pendiente_y.text()) > 0:
            y_1 = float(self.ui.txt_pendiente_y.text())
        else:
            self.advertencias.setText("No ha ingresado la coordenada y_1")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_pendiente_x_2.text()) > 0:
            x_2 = float(self.ui.txt_pendiente_x_2.text())
        else:
            self.advertencias.setText("No ha ingresado la coordenada x_2")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_pendiente_y_2.text()) > 0:
            y_2 = float(self.ui.txt_pendiente_y_2.text())
        else:
            self.advertencias.setText("No ha ingresado la coordenada y_2")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        M = (y_2-y_1)/(x_2-x_1)
        self.ui.lbl_solucion_pendiente.setText(str(M))

    def cuadratica(self):
        if len(self.ui.txt_cuadratica_a.text()) > 0:
            a = float(self.ui.txt_cuadratica_a.text())
            print(a)
        else:
            self.advertencias.setText("No ha ingresado el termino a")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_cuadratica_b.text()) > 0:
            b = float(self.ui.txt_cuadratica_b.text())
        else:
            self.advertencias.setText("No ha ingresado el termino b")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_cuadratica_c.text()) > 0:
            c = float(self.ui.txt_cuadratica_c.text())
        else:
            self.advertencias.setText("No ha ingresado el termino c")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        I = ((b ** 2) - (4 * (a * c)))
        if I >= 0:
            R = math.sqrt(I)
            S_1 = (((-1 * b) + R) / (2 * a))
            S_2 = (((-1 * b) - R) / (2 * a))
            SR1 = round(S_1, 3)
            SR2 = round(S_2, 3)
            print("x1=", SR1)
            print("x2=", SR2)
            self.ui.lbl_solucion_cuadratica.setText("x_1= {} \t x_2 {}".format(SR1,SR2))
        else:
            self.ui.lbl_solucion_cuadratica.setText("SIN SOLUCION")
    def sumar(self):
        if len(self.ui.txt_num_1.text()) > 0:
            x_1 =  int(self.ui.txt_num_1.text())
        else:
            self.advertencias.setText("No ha ingresado el numero 1")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_num_2.text()) > 0:
            x_2 = int(self.ui.txt_num_2.text())
        else:
            self.advertencias.setText("No ha ingresado el numero 2")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        s = x_1 +x_2
        print(s)
        self.ui.lbl_inicio_saludo_5.setVisible(True)
        self.ui.lbl_resultado_oper_basicas.setText(str(s))
    def multiplicar(self):
        if len(self.ui.txt_num_1.text()) > 0:
            x_1 =  int(self.ui.txt_num_1.text())
        else:
            self.advertencias.setText("No ha ingresado el numero 1")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        if len(self.ui.txt_num_2.text()) > 0:
            x_2 = int(self.ui.txt_num_2.text())
        else:
            self.advertencias.setText("No ha ingresado el numero 2")
            self.advertencias.setIcon(QMessageBox.Critical)
            self.advertencias.setWindowTitle("Error")
            self.advertencias.exec_()
        m = x_1 * x_2
        self.ui.lbl_inicio_saludo_5.setVisible(True)
        self.ui.lbl_resultado_oper_basicas.setText(str(m))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Funciones_calculadora()
    ui.show()
    sys.exit(app.exec_())
