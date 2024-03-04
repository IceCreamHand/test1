import sys  #系统文件操作
#sys.path.append("aaa")
#from aaa import ttt
import test
from PyQt5.QtWidgets import QApplication,QMainWindow
##这只是一个测试
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow1 = QMainWindow()  # MainWindow1随便改
    ui = test.Ui_MainWindow()  # 随便改
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_()) #app.exec_()死循环来监听界面关闭按钮等界面控件事件


