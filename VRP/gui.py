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
        self.program = Program()
        self.program.ImportData()
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.program.SelectData(self.names)
        self.program.InitializePopulation(1,100)
        #self.interface()

    def interface(self):

        self.resize(640, 480)
        #self.setWindowTitle("")
        checkboxes = []
        for i in range(0,len(self.program.GetNames())):
            cb = QCheckBox(self.program.GetNames()[i], self)
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
        #print('clicked')
        self.program.SelectData(self.names)
        #self.program.ShowData()
        self.program.InitializePopulation(1,100)
        #self.program.ShowPopulation()
        self.program.ShowLengths()
        for i in range(0,1):
            self.program.PlayRound()

        self.program.ShowLengths()
        self.program.ShowBest()


    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            #print("selected")
            #print(self.sender().text())
            if self.sender().text() not in self.names:
                self.names.append(self.sender().text())
        else:
            self.names.remove(self.sender().text())


   