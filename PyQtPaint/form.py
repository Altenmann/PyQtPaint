
from typing import Sequence
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt, pyqtSignal
from PyQtPaint.objects import PainterObject

class PainterWindow(QMainWindow):
    update_signal = pyqtSignal()

    def __init__(self, **kwargs):
        super().__init__()
        self.setWindowTitle("Painter Window")
        if kwargs.get('fullscreen', False):
            self.showFullScreen()
        else:
            width, height = kwargs.get('width', 500), kwargs.get('height', 500)
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
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(self.rect())
        for obj in self.painter_objects:
            obj.paint(painter)
        painter.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)
