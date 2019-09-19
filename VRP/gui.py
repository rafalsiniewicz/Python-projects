#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QButtonGroup, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5 import QtCore
from functools import partial
from program import *
from map import *
import folium
import geocoder
import webbrowser
import webview
import os 
from PySide2 import *
import sys
from PySide2.QtWidgets import QApplication, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView



CRACOW_CENTRE = {"CRACOW": [50.061681, 19.938104]}

class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.program = Program()
        self.program.ImportData()
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.program.SelectData(self.names)
        #self.program.InitializePopulation(3,100)
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
        #print(self.names)
        self.program.SelectData(self.names)
        #self.program.ShowData()
        self.program.InitializePopulation(3,100)
        #self.program.ShowPopulation()
        self.program.GetPopulation().AddStart(START,END)
        self.program.GetPopulation().SortPopulation()
        self.program.ShowLengths()
        self.program.GetPopulation().RemoveStart()
        
        for i in range(0,1):
            self.program.PlayRound()

        self.program.ShowLengths()
        self.program.ShowBest()
        print(self.program.GetPopulation().BestIndividual().GetLength())
        self.create_map(self.program)

    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            #print("selected")
            #print(self.sender().text())
            if self.sender().text() not in self.names:
                self.names.append(self.sender().text())
        else:
            self.names.remove(self.sender().text())


    def create_map(self, program):
        m = folium.Map(location=[CRACOW_CENTRE["CRACOW"][0], CRACOW_CENTRE["CRACOW"][1]],
            zoom_start=15, control_scale=True)


        for place, position in self.program.GetPopulation().BestIndividual().Merge().items():
            folium.Marker(
                location=[position[0], position[1]],
                popup=place,
                icon=folium.Icon(color='green', icon='ok-sign'),
            ).add_to(m)
            outfp = "map.html"
            m.save(outfp)
        #webview.create_window('Hello world', 'map.html')

        #app = QApplication(sys.argv)
        #label = QLabel("Hello World!")
        self.browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.browser.load(local_url)

        self.browser.show()



