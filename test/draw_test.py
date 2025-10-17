from PyQtPaint import App, PainterObject
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPointF

class TestCircle(PainterObject):
	def __init__(self, x, y, r):
		super().__init__(brushColor = QColor(200, 0, 0))
		self.x, self.y, self.r = x, y, r

	def paint(self, painter: QPainter):
		super().paint(painter)

		center = QPointF(self.x, self.y)
		painter.drawEllipse(center, self.r, self.r)

class DrawApp(App):
	def __init__(self):
		super().__init__()
	
	def setup_objects(self):
		self.circle = TestCircle(100, 100, 10)
		self.window.add_painter_object(self.circle)

	def update(self):
		self.circle.y += .1

if __name__ == "__main__":
	app = DrawApp()
	app.run()