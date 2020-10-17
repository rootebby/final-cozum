from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap
from selenium import webdriver
import sys

"""
http://www.final.com.tr/anasayfa.aspx?s=testCozum&id=984&c=lof2j5
lof2j5
"""


class Final(QWidget):
    def __init__(self):
        super().__init__()
        self.ebby()

    def ebby(self):
        self.ebby = QLabel("coded by root@ebby:~#")
        self.text = QLabel("Hoşgeldin\nKimya")
        self.link = QLineEdit("Kodu Buraya Yaz - vblf4y")
        self.arama = QPushButton("Ara")
        self.temizle = QPushButton("Temizle")
        self.resim = QLabel()
        self.resim.setPixmap(QPixmap("asd.png"))

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addStretch()
        vbox.addWidget(self.ebby)
        vbox.addStretch()
        vbox.addWidget(self.text)
        vbox.addWidget(self.link)
        vbox.addWidget(self.arama)
        vbox.addWidget(self.temizle)
        vbox.addStretch()

        hbox.addStretch()
        hbox.addWidget(self.resim)
        hbox.addLayout(vbox)
        hbox.addStretch()

        self.setLayout(hbox)

        self.arama.clicked.connect(self.search)
        self.temizle.clicked.connect(self.clear)

        self.setWindowTitle("Final Video Çözüm - Kimya")
        self.show()

    def search(self):
	    browser = webdriver.Firefox()
	    browser.get("http://www.final.com.tr/anasayfa.aspx?s=testCozum&id=984&c={}".format(self.link.text()))

    def clear(self):
        self.link.clear()


app = QApplication(sys.argv)
final = Final()
sys.exit(app.exec_())











