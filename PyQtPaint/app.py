
import sys, threading, time
from typing import Callable
from PyQt5.QtWidgets import QApplication
from PyQtPaint.form import PainterWindow


def setup_app(width: int, height: int):
    global screen_width, screen_height
    screen_width = width
    screen_height = height

def run_app(
        init_objects: Callable[[PainterWindow], None],
        update: Callable[[PainterWindow], None], 
        fps: int
):
    '''
    Will run a thread of the given update method
    Will also run an PyQt5 QApplication thread
    '''
    
    global window, screen_width, screen_height

    update_time = 1/fps

    def wrapper():
        while True:
            # Wait for window to be defined
            try:
                if(type(window) == PainterWindow):
                    break
            except NameError:
                time.sleep(1)

        init_objects(window)

        # The main thread loop
        while True:
            update(window)
            window.update_signal.emit()
            time.sleep(update_time)

    threading.Thread(target=wrapper, daemon=True).start()

    # Initialize app
    app = QApplication(sys.argv)

    window = PainterWindow(screen_width, screen_height)
    window.show()

    # Run app loop
    sys.exit(app.exec_())



