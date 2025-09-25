
import sys, threading, time
from PyQt5.QtWidgets import QApplication
from PyQtPaint.form import PainterWindow
from abc import ABC, abstractmethod

class App(ABC):
    '''An abstract class to setup and run a painter window.'''

    def __init__(self, **kwargs):
        self.fps = kwargs.pop('fps', 30)
        self.init_qapp(**kwargs)

    def init_qapp(self, **kwargs):
        self.app = QApplication(sys.argv)
        self.window = PainterWindow(**kwargs)

        # Define width and height from the window after defined
        self.width = self.window.width()
        self.height = self.window.height()

    def run(self):
        '''Starts an update thread and the app thread.'''
        self.window.show()
        self.window.destroyed.connect(lambda: setattr(self, "window_closed", True))

        threading.Thread(target=self.update_wrapper, daemon=True).start()
        sys.exit(self.app.exec_())

    def update_wrapper(self):
        update_time = 1/self.fps

        self.setup_objects()

        # Update loop
        while not getattr(self, "window_closed", False):
            self.update()
            self.window.update_signal.emit()
            time.sleep(update_time)

    @abstractmethod
    def update(self): 
        '''Update calls every so often based on self.fps'''
        pass

    @abstractmethod
    def setup_objects(self): 
        '''Add objects to the self.window PainterWindow'''
        pass
