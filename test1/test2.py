import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
w = QWidget()#窗体
w.setWindowTitle("刘金玉编程")
w.resize(400,300)
w.setWindowIcon(QIcon("img/img.png"))
w.setToolTip("编程创造一个城市")

btn = QPushButton("老刘",w)#按钮控件
btn.setToolTip("刘金玉编程")

w.show()
#第二个窗体
#w2 = QWidget()
#w2.setWindowIcon(QIcon("img/img.png"))#QWidget设置出来的图标是每个窗体，而QApplication的setwindowQIcon则会设置所有窗体图标(mac系统仅能识别）
#w2.show()


app.exec_()
