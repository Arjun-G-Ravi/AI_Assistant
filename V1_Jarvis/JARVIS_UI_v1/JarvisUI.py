from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt


class Ui_JarvisGUI(object):
    def setupUi(self, JarvisGUI):
            JarvisGUI.setObjectName("MainWindow")
            JarvisGUI.resize(1366, 760)
            self.centralwidget = QtWidgets.QWidget(JarvisGUI)
            self.centralwidget.setObjectName("centralwidget")
            
            self.BackGround = QtWidgets.QLabel(self.centralwidget)
            self.BackGround.setGeometry(QtCore.QRect(0, 0, 1366, 760))
            self.BackGround.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
            self.BackGround.setText("")
            self.BackGround.setPixmap(QtGui.QPixmap("JARVIS_UI_v1\Black_Template.jpg"))
            self.BackGround.setScaledContents(True)
            self.BackGround.setObjectName("BackGround")

            self.JARVIS = QtWidgets.QLabel(self.centralwidget)
            self.JARVIS.setGeometry(QtCore.QRect(710, 20, 531, 471))
            self.JARVIS.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
            self.JARVIS.setText("")
            self.JARVIS.setPixmap(QtGui.QPixmap("JARVIS_UI_v1\InkedHD-wallpaper-jarvis-artificial-intelligence-iron-man-marvel_LI.jpg"))
            self.JARVIS.setScaledContents(True)
            self.JARVIS.setObjectName("JARVIS")

            self.violet = QtWidgets.QLabel(self.centralwidget)
            self.violet.setGeometry(QtCore.QRect(-80, -100, 471, 351))
            self.violet.setText("")
            self.violet.setObjectName("violet")
            self.violet.setAlignment(Qt.AlignCenter)
            self.violet.setScaledContents(True)
            self.movie = QMovie("JARVIS_UI_v1\Siri_1.gif")
            self.violet.setMovie(self.movie)
            self.movie.start()

            self.globalNetwork = QtWidgets.QLabel(self.centralwidget)
            self.globalNetwork.setGeometry(QtCore.QRect(240, 50, 421, 241))
            self.globalNetwork.setText("")
            self.globalNetwork.setObjectName("globalNetwork")
            self.globalNetwork.setAlignment(Qt.AlignCenter)
            self.globalNetwork.setScaledContents(True)
            self.movie = QMovie("JARVIS_UI_v1\Earth_Template.gif")
            self.globalNetwork.setMovie(self.movie)
            self.movie.start()
            
            self.BigScreenWithJarvAndInitiatingSys = QtWidgets.QLabel(self.centralwidget)
            self.BigScreenWithJarvAndInitiatingSys.setGeometry(QtCore.QRect(10, 350, 541, 331))
            self.BigScreenWithJarvAndInitiatingSys.setText("")
            self.BigScreenWithJarvAndInitiatingSys.setObjectName("BigScreenWithJarvAndInitiatingSys")
            self.BigScreenWithJarvAndInitiatingSys.setAlignment(Qt.AlignCenter)
            self.BigScreenWithJarvAndInitiatingSys.setScaledContents(True)
            self.movie = QMovie("JARVIS_UI_v1\Jarvis_Gui (2).gif")
            self.BigScreenWithJarvAndInitiatingSys.setMovie(self.movie)
            self.movie.start()
            
            self.Suit = QtWidgets.QLabel(self.centralwidget)
            self.Suit.setGeometry(QtCore.QRect(20, 170, 261, 161))
            self.Suit.setText("")
            self.Suit.setObjectName("Suit")
            self.Suit.setAlignment(Qt.AlignCenter)
            self.Suit.setScaledContents(True)
            self.movie = QMovie("JARVIS_UI_v1\live.gif")
            self.Suit.setMovie(self.movie)
            self.movie.start()           
            
            self.audioSpectrum = QtWidgets.QLabel(self.centralwidget)
            self.audioSpectrum.setGeometry(QtCore.QRect(760, 550, 441, 141))
            self.audioSpectrum.setText("")
            self.audioSpectrum.setObjectName("audioSpectrum")
            self.audioSpectrum.setAlignment(Qt.AlignCenter)
            self.audioSpectrum.setScaledContents(True)
            self.movie = QMovie("JARVIS_UI_v1\audioSpectrum.gif")
            self.audioSpectrum.setMovie(self.movie)
            self.movie.start()            
            
            JarvisGUI.setCentralWidget(self.centralwidget)

            self.retranslateUi(JarvisGUI)
            QtCore.QMetaObject.connectSlotsByName(JarvisGUI)

    
    def retranslateUi(self, JarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisGUI.setWindowTitle(_translate("JarvisGUI", "JARVIS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisGUI()
    ui.setupUi(JarvisGUI)
    JarvisGUI.show()
    sys.exit(app.exec_())