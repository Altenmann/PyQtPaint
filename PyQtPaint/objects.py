
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF
from PyQt5.QtCore import Qt, QPointF
from abc import ABC, abstractmethod

class PainterObject(ABC):
    def __init__(self, **kwargs):
        brushColor = kwargs.get("brushColor", Qt.white)
        penColor = kwargs.get("penColor", Qt.white)
        self._isPen = True
        self._isBrush = True
        self.set_color(brushColor, penColor)

    def set_isPen(self, isPen): self._isPen = isPen
    def set_isBrush(self, isBrush): self._isBrush = isBrush

    def set_color(self, brushColor, penColor):
        self._brushColor = brushColor
        self._penColor = penColor
        if not hasattr(self, "_brush"): self._brush = QBrush(brushColor) 
        else: self._brush.setColor(brushColor)
        if not hasattr(self, "_pen"): self._pen = QPen(penColor) 
        else: self._pen.setColor(penColor)

    def set_line_width(self, width: float):
        self._pen.setWidthF(width)

    def painter_brush_and_pen(self, painter: QPainter):
        if self._isBrush: painter.setBrush(self._brush)
        else: painter.setBrush(QBrush())
        if self._isPen: painter.setPen(self._pen)
        else: painter.setPen(Qt.NoPen)

    @abstractmethod
    def paint(self, painter: QPainter):
        self.painter_brush_and_pen(painter)

# PainterObject for drawing rectangles
class PRectangle(PainterObject):
    def __init__(self, x, y, width, height, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def paint(self, painter: QPainter):
        super().paint(painter)

        x = int(self.x)
        y = int(self.y)
        w = int(self.width)
        h = int(self.height)
        
        painter.drawRect(x, y, w, h)

# PainterObject for drawing lines
class PLine(PainterObject):
    def __init__(self, x1, y1, x2, y2, **kwargs):
        super().__init__(**kwargs)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.set_line_width(1)
    
    def paint(self, painter: QPainter):
        super().paint(painter)

        x1 = int(self.x1)
        y1 = int(self.y1)
        x2 = int(self.x2)
        y2 = int(self.y2)
        
        painter.drawLine(x1, y1, x2, y2)

# PainterObject for drawing polygons
class PPolygon(PainterObject):
    def __init__(self, xs, ys, **kwargs):
        super().__init__(**kwargs)
        if len(xs) != len(ys):
            raise ValueError("xs and ys must have the same length")
        
        self.points = []
        for i in range(len(xs)):
            self.points.append(QPointF(xs[i], ys[i]))

    def paint(self, painter: QPainter):
        super().paint(painter)
        painter.drawPolygon(QPolygonF(self.points))

class PCircle(PainterObject):
    def __init__(self, x, y, r, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.r = r

    def paint(self, painter: QPainter):
        super().paint(painter)

        x = int(self.x - self.r)
        y = int(self.y - self.r)
        s = int(self.r*2)
        painter.drawEllipse(x, y, s, s)
