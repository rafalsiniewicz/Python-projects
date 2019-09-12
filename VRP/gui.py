#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QButtonGroup, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from functools import partial
from program import *



class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #self.interface()

    def interface(self, places):

        self.resize(640, 480)
        #self.setWindowTitle("")
        checkboxes = []
        for i in range(0,len(places)):
            cb = QCheckBox(places[i], self)
            cb.move(20 + 30 * (i*20//460), 20 + i * 20 % 460)
            #print(cb.text())
            cb.toggle()
            checkboxes.append(cb)



        for i in checkboxes:
            i.stateChanged.connect(self.checkBoxChangedAction)

        button = QPushButton('Calculate track', self)
        button.setToolTip('This is an example button')
        button.move(200,70)
        button.clicked.connect(self.on_click)
        
        self.show()

    def on_click(self):
        print('clicked')

    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            print("selected")
            #print(self.sender())
        else:
            print("not selected")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()
    program = Program()
    program.ImportData()
    window.interface(program.GetNames())
    '''program = Program()
    program.ImportData()
    program.InitializePopulation()
    program.ShowBest()'''
    sys.exit(app.exec_())

   