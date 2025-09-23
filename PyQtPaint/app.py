
import sys, threading, time
from typing import Callable
from PyQt5.QtWidgets import QApplication
from PyQtPaint.form import PainterWindow
from abc import ABC, abstractmethod

class App(ABC):
    '''
    An abstract class to setup and run a painter window.
    Usage:
    ```python
    app = SubApp()
    app.run()
    ```
    '''

    def __init__(self, **kwargs):
        '''
        Use `fullscreen=True` or use `width=(int)` and `height=(int)`.
        Use `fps=(int)` to choose how often it updates defaults to 30.
        '''
        self.setup_app(**kwargs)

    def run(self):
        '''Starts an update thread and the app thread.'''
        # Start the update thread
        threading.Thread(target=self.update_wrapper, daemon=True).start()

        # Initialize app
        app = QApplication(sys.argv)

        self.window = PainterWindow(
            fullscreen=self.fullscreen, 
            width=self.screen_width, 
            height=self.screen_height
        )
        self.window.show()

        # Run app loop
        sys.exit(app.exec_())

    def setup_app(self, **kwargs):
        self.screen_width = kwargs.get('width', 500)
        self.screen_height = kwargs.get('height', 500)
        self.fullscreen = kwargs.get('fullscreen', False)
        self.fps = kwargs.get('fps', 30)

    def update_wrapper(self):
        update_time = 1/self.fps
        while True: # Wait for window to be initialized
            try:
                if hasattr(self, "window"):
                    break
            except NameError:
                time.sleep(1)

        self.setup_objects()

        # The main thread loop
        while self.window.isVisible():
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
