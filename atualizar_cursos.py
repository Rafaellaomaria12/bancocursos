import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon
 
cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="123@senac",
    database="tbcursos"
)
 
cursor = cx.cursor()
 
class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()
 
        layout = QVBoxLayout()
 
        self.setGeometry(500,300,450,350)
        self.setWindowTitle("Cursos cadastrados")
       
       
        labelId = QLabel("Id curso: ")
        self.editId = QLineEdit()
 
 
        labelCurs = QLabel("Nome do curso: ")
        self.editCurs = QLineEdit()
 
        labelChor = QLabel("Carga horária: ")
        self.editChor = QLineEdit()
 
 
        psbCadastro = QPushButton("Atualizar")
       
       
        layout.addWidget(labelId)
        layout.addWidget(self.editId)
 
 
        layout.addWidget(labelCurs)
        layout.addWidget(self.editCurs)
 
        layout.addWidget(labelChor)
        layout.addWidget(self.editChor)
 
       
        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCli)
 
 
        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(10)
 
        headerLine=["Id","Nome","Carga Horaria"]
 
        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from registrodecursos")
 
        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(str(linha[1])))
            tbcursos.setItem(lintb,2,QTableWidgetItem(str(linha[2])))
            lintb+=1
 
       
        layout.addWidget(tbcursos)
        self.setLayout(layout)
 
    def upCli (self):
        if (self.editId.text()==""):
            print("Não é possível atualizar sem o Id do curso")
       
        elif(self.editCurs.text()=="" and self.editChor.text()==""):
            print("Não é possível atualizar se não houver dados")
 
        elif(self.editCurs.text()!="" and self.editChor.text()==""):
            cursor.execute("update registrodecursos set nome_cursos=%s where cursos_id=%s",
                           (self.editCurs.text(), self.editId.text()))
           
        elif(self.editCurs.text()=="" and self.editChor.text()!=""):
            cursor.execute("update registrodecursos set carga_horaria=%s where cursos_id=%s",
                           (self.editChor.text(), self.editId.text()))
           
        else:
            cursor.execute("update registrodecursos set nome_cursos=%s, carga_horaria=%s where cursos_id=%s",
                           (self.editCurs.text(), self.editChor.text(), self.editId.text()))
           
        cx.commit()
        print("Todas modificações foram realizadas")
           
           
 
if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())