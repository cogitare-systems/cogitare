__author__ = 'vbaptistel'

import os, sys
import mysql.connector
import password_crypt

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.loginUI import Ui_MainWindow

TRYS = 1

def autenticar():
    global TRYS
    usuario = ui.user_txtfield.text()
    senha = password_crypt.encrypt(ui.password_txtfield.text())
    db = dbConnect()
    cursor = db.cursor()
    query = "SELECT username, password FROM cad_usuarios WHERE username = '" + usuario + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    if not rows:
        ui.mensagem_label.setHidden(False)
        print("Usuario nao existe!")
    else:
        for (u, p) in rows:
            if p == senha:
                ui.mensagem_label.setHidden(True)
                print("autenticado!")
                TRYS = 0
            else:
                ui.mensagem_label.setHidden(False)
                print("senha incorreta!")
                TRYS = TRYS + 1
            break
        print(TRYS)
    cursor.close()
    db.close()

def dbConnect():
    config = {
        'user': 'root',
        'password': 'Vin1987@',
        'host': '127.0.0.1',
        'database': 'cogitare_db',
        'port': 3307 }
    con = mysql.connector.connect(**config)
    return con

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.mensagem_label.setHidden(True)
    ui.logo_label.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/principia_logo.png"))
    ui.copyright_label.setText(u"\N{COPYRIGHT SIGN}" + " 2015 Cogitare Systems")
    ui.login_btn.clicked.connect(autenticar)

    window.show()
    sys.exit(app.exec_())


