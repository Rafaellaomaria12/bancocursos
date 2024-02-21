import sys
 
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mc
 
con = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="123@senac",
    database="tbcursos"
)
cursor = con.cursor()

class ExibirCurso(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300,400,450,300)
        self.setWindowTitle("Cursos cadastrados")
        
        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(10)

        headerLine=["Id","curso","carga horaria"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from registrodecursos")
        lintb = 0
        
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1
           
        layout= QVBoxLayout()
        layout.addWidget(tbcursos)
        self.setLayout(layout)          
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = ExibirCurso()
    tela.show()
    sys.exit(app.exec_())