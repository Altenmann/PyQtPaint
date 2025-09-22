
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF
from PyQt5.QtCore import Qt, QPointF
from abc import ABC, abstractmethod

class PainterObject(ABC):
    def __init__(self, color):
        self._brush = QBrush(color)
        self._pen = QPen(color)

    def set_color(self, color):
        self._brush.setColor(color)
        self._pen.setColor(color)

    def set_line_width(self, width: float):
        self._pen.setWidthF(width)

    @abstractmethod
    def paint(self, painter: QPainter): pass

# PainterObject for drawing rectangles
class PRectangle(PainterObject):
    def __init__(self, x, y, width, height, color=Qt.white):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def paint(self, painter: QPainter):

        x = int(self.x)
        y = int(self.y)
        w = int(self.width)
        h = int(self.height)
        cx = x-int(w/2)
        cy = y-int(h/2)
        
        painter.setBrush(self._brush)
        painter.setPen(Qt.NoPen)
        painter.drawRect(cx, cy, w, h)

# PainterObject for drawing lines
class PLine(PainterObject):
    def __init__(self, x1, y1, x2, y2, color=Qt.white):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.set_line_width(1)
    
    def paint(self, painter: QPainter):
        x1 = int(self.x1)
        y1 = int(self.y1)
        x2 = int(self.x2)
        y2 = int(self.y2)
        
        painter.setPen(self._pen)
        painter.drawLine(x1, y1, x2, y2)

# PainterObject for drawing polygons
class PPolygon(PainterObject):
    def __init__(self, xs, ys, color=Qt.white):
        super().__init__(color)
        if len(xs) != len(ys):
            raise ValueError("xs and ys must have the same length")
        
        self.points = []
        for i in range(len(xs)):
            self.points.append(QPointF(xs[i], ys[i]))

    def paint(self, painter: QPainter):
        painter.setBrush(self._brush)
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(QPolygonF(self.points))

class PCircle(PainterObject):
    def __init__(self, x, y, r, color=Qt.white):
        super().__init__(color)
        self.x = x
        self.y = y
        self.r = r

    def paint(self, painter: QPainter):
        painter.setBrush(self._brush)
        painter.setPen(Qt.NoPen)

        x = int(self.x - self.r)
        y = int(self.y - self.r)
        s = int(self.r*2)
        painter.drawEllipse(x, y, s, s)
