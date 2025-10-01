
import sys, threading, time
from PyQt5.QtWidgets import QApplication
from PyQtPaint.form import PainterWindow
from abc import ABC, abstractmethod

class App(ABC):
    '''An abstract class to setup and run a painter window.'''

    def __init__(self, **kwargs):
        self.auto_updates = kwargs.pop('auto_update', True)
        self.fps = kwargs.pop('fps', 30)
        self.init_qapp(**kwargs)

    def init_qapp(self, **kwargs):
        self.app = QApplication(sys.argv)
        self.window = PainterWindow(**kwargs)

        # Define width and height from the window after defined
        self.width = self.window.width()
        self.height = self.window.height()

        # Wire up event handlers to forward to App methods
        self.window.on_mouse_press = self.on_mouse_press
        self.window.on_mouse_release = self.on_mouse_release
        self.window.on_mouse_double_click = self.on_mouse_double_click
        self.window.on_mouse_move = self.on_mouse_move
        self.window.on_mouse_enter = self.on_mouse_enter
        self.window.on_mouse_leave = self.on_mouse_leave
        self.window.on_mouse_wheel = self.on_mouse_wheel
        self.window.on_key_press = self.on_key_press
        self.window.on_key_release = self.on_key_release

    def run(self):
        '''Starts an update thread and the app thread.'''
        self.window.show()
        self.window.destroyed.connect(lambda: setattr(self, "window_closed", True))
        
        self.setup_objects()
        if self.auto_updates:
            threading.Thread(target=self.update_wrapper, daemon=True).start()
        sys.exit(self.app.exec_())

    def update_wrapper(self):
        update_time = 1/self.fps

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

    # --- Event Handler Methods (Override these in subclasses) ---
    # Mouse events
    def on_mouse_press(self, event): pass
    def on_mouse_release(self, event): pass
    def on_mouse_double_click(self, event): pass
    def on_mouse_move(self, event): pass
    def on_mouse_enter(self, event): pass
    def on_mouse_leave(self, event): pass
    def on_mouse_wheel(self, event): pass
    
    # Keyboard events
    def on_key_press(self, event): pass
    def on_key_release(self, event): pass
