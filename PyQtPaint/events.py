
class MouseHandler:
    # Mousetracking=True for capturing mouse movement without mouse down
    def __init__(self, mouse_tracking=False):
        self.mouse_tracking = mouse_tracking
    
    # Event methods to be overriden
    def press(self, event): pass
    def release(self, event): pass
    def double(self, event): pass
    def move(self, event): pass
    def enter(self, event): pass
    def leave(self, event): pass
    def wheel(self, event): pass

class KeyHandler:
    def press(self, event): pass
    def release(self, event): pass