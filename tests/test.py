
import sys, threading, time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QPointF
from PyQtPaint.form import PainterWindow
from PyQtPaint.painter_objects import PPolygon, PRectangle

def update_window():
    global window
    
    xs = [100, 200, 250, 50]
    ys = [100, 100, 200, 200]
    poly1 = PPolygon(xs, ys)

    isShape = False
    while not isShape:
        time.sleep(1)
        if window is not None:
            window.add_painter_object(poly1)
            window.update_signal.emit()
            isShape = True

    while True:
        for i in range(poly1.polygon.count()):
            point = poly1.polygon.at(i)
            dx, dy = .1, .1 
            new_point = QPointF(point.x() + dx, point.y() + dy)
            poly1.polygon.replace(i, new_point)
        window.update_signal.emit()
        time.sleep(0.1)
        

def run_app():
    global window

    # Initialize app
    app = QApplication(sys.argv)

    width, height = 800, 800
    window = PainterWindow(width, height)
    window.show()

    # Run app loop
    sys.exit(app.exec_())


threading.Thread(target=update_window, daemon=True).start()

run_app()