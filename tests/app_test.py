
from PyQtPaint.form import PainterWindow
from PyQtPaint.app import setup_app, run_app
from PyQtPaint.objects import PLine, PPolygon

def create_objects(width, height):
    global poly1, xlines, ylines
    xlines = []
    ylines = []
    for i in range(11):
        x = i * (width-1)/10
        y = i * (height-1)/10
        xlines.append(PLine(x, 0, x, height))
        ylines.append(PLine(0, y, width, y))

    xs = [100, 200, 250, 50]
    ys = [100, 100, 200, 200]
    poly1 = PPolygon(xs, ys)

def init_objects(window: PainterWindow):
    global poly1, xlines, ylines
    create_objects(window.width(), window.height())
    window.add_painter_objects(xlines)
    window.add_painter_objects(ylines)
    window.add_painter_object(poly1)

def update(window: PainterWindow):
    global poly1
    for point in poly1.points:
        point.setX(point.x() + 1)
        point.setY(point.y() + 1)

# setup_app(fullscreen=True)
setup_app(width=600, height=600)
run_app(init_objects, update, 30)
