from PyQt5 import QtCore, QtWidgets
from matplotlib import pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.XlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.XlineEdit.setGeometry(QtCore.QRect(130, 60, 371, 41))
        self.XlineEdit.setObjectName("XlineEdit")
        self.YlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.YlineEdit.setGeometry(QtCore.QRect(130, 170, 371, 41))
        self.YlineEdit.setObjectName("YlineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 91, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotter"))
        self.label.setText(_translate("MainWindow", "X points"))
        self.label_2.setText(_translate("MainWindow", "Y points"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))

    def click(self):
        XpointsString = self.XlineEdit.text()
        x_list = XpointsString.split(',')
        x_list1 = list(map(float, x_list))

        YpointsString = self.YlineEdit.text()
        y_list = YpointsString.split(',')
        y_list1 = list(map(float, y_list))
        self.plot(x_list1,y_list1)
        
    def plot(self,xpoints,ypoints):
        x_points = xpoints
        y_points = ypoints
        self.sle(x_points,y_points) #solving linear equations       

    def sle(self,x,y):
        xpoints = x
        ypoints = y
        sigx = sum(x)
        sigy = sum(y)
        sigxsq = 0
        for sq in x:
            sigxsq += sq**2
        n = len(x)
        sigxy = 0
        yindex = 0
        for i in x:
            res = i*y[yindex]
            yindex += 1
            sigxy += res

        eq1 = [sigx,sigxsq,sigxy] 
        eq2 = [n,sigx,sigy]

        def solveLinearEquations():
            a1 = [(eq1[0]/eq1[0]),(eq1[1]/eq1[0]),(eq1[2]/eq1[0])]

            b1 = [(eq2[0]/eq2[0]),(eq2[1]/eq2[0]),(eq2[2]/eq2[0])]

            eq11 = [(a1[0]-b1[0]),(a1[1]-b1[1]),(a1[2]-b1[2])]

            y = eq11[2]/eq11[1]

            a21 = [a1[0],a1[1]*y,a1[2]]

            x = a21[2]-a21[1]
            x = round(x,4)
            y = round(y,4)
            return x, y
        final = solveLinearEquations()
        final = list(final)
        a_value = final[0]
        b_value = final[1]

        slope = b_value
        intercept = a_value

        self.lineForm(slope, intercept,xpoints,ypoints)

    def lineForm(self, slope, intercept,Oldx,Oldy):
        print('Y =',slope,'\bx+',intercept)
        y = []
        for i in Oldx:
            ypoint = (slope*i)+intercept
            y.append(ypoint)

        plt.plot(Oldx,Oldy, marker = 'o')
        plt.plot(Oldx,y)
        plt.show()
                                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
