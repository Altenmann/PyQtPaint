
from typing import Sequence
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt, pyqtSignal
from PyQtPaint.painter_objects import PainterObject

class PainterWindow(QMainWindow):
    update_signal = pyqtSignal()

    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("Painter Window")
        self.setGeometry(100, 100, width, height)
        self.painter_objects = []

        self.update_signal.connect(self.update)
    
    def add_painter_object(self, obj: PainterObject):
        self.painter_objects.append(obj)

    def add_painter_objects(self, objs: Sequence[PainterObject]):
        for obj in objs:
            self.add_painter_object(obj)

    def remove_painter_object(self, obj: PainterObject):
        if obj in self.painter_objects:
            self.painter_objects.remove(obj)
    
    def remove_painter_objects(self, objs: Sequence[PainterObject]):
        for obj in objs:
            self.remove_painter_object(obj)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(self.rect())
        for obj in self.painter_objects:
            obj.paint(painter)
        painter.end()
