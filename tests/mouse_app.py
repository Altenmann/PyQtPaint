
# App to test mouse handling

from PyQtPaint import App, PCircle
from PyQt5.QtGui import QColor, QLinearGradient
from PyQt5.QtCore import QPoint, Qt

radius = 25
mouseCircle = PCircle(0, 0, radius, brushColor=QColor("#000000"))
mouseCircle.set_isPen(False)

background_grad = QLinearGradient()
background_grad.setStops([
    (0, QColor("#000000")),
    (0.5, QColor("#00AAFF")),
    (1, QColor("#000000"))
])

class MouseApp(App):
    def __init__(self):
        super().__init__(
            title='Mouse App',
            width=800, height=800,
            mouse_tracking = True,
            background=background_grad
        )
        cx = int(self.width/2)
        background_grad.setStart(QPoint(cx, 0))
        background_grad.setFinalStop(QPoint(cx, self.height))

        self.window.setCursor(Qt.CursorShape.BlankCursor)

    def mouseMove(self, event):
        mouseCircle.x = event.pos().x()
        mouseCircle.y = event.pos().y()

        newStops = background_grad.stops()
        midFloat = min(.99, max(.01, event.pos().y()/self.height))
        newStops[1] = (midFloat, newStops[1][1])
        background_grad.setStops(newStops)
        
    def setup_objects(self):
        self.window.add_painter_object(mouseCircle)

    def update(self):
        pass


if __name__ == "__main__":
    app = MouseApp()
    app.run()