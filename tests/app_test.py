
from PyQtPaint.form import PainterWindow
from PyQtPaint.app import setup_app, run_app
from PyQtPaint.painter_objects import PLine


width, height = 600, 600

xlines = []
ylines = []
for i in range(11):
    x = i * (width-1)/10
    y = i * (height-1)/10
    xlines.append(PLine(x, 0, x, height))
    ylines.append(PLine(0, y, width, y))


def init_objects(window: PainterWindow):
    window.add_painter_objects(xlines)
    window.add_painter_objects(ylines)

def update(window: PainterWindow):
    pass


setup_app(width, height)
run_app(init_objects, update, 30)
