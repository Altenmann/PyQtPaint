
import sys, threading, time
from typing import Callable
from PyQt5.QtWidgets import QApplication
from PyQtPaint.form import PainterWindow


def setup_app(**kwargs):
    '''Use `fullscreen=True` or use `width=(int)` and `height=(int)`'''
    global screen_width, screen_height, fullscreen
    screen_width = kwargs.get('width')
    screen_height = kwargs.get('height')
    fullscreen = kwargs.get('fullscreen', False)

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

    def update_wrapper():
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

    threading.Thread(target=update_wrapper, daemon=True).start()

    # Initialize app
    app = QApplication(sys.argv)

    window = PainterWindow(fullscreen=fullscreen, width=screen_width, height=screen_height)
    window.show()

    # Run app loop
    sys.exit(app.exec_())



