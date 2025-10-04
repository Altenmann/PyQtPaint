# Comprehensive demo showing all available event handlers

from PyQtPaint import App, PRectangle, PCircle, PText
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class EventsDemoApp(App):
    def __init__(self):
        super().__init__(
            title='Events Demo - Press ESC to exit',
            width=800, height=600,
            mouse_tracking=True  # Enable mouse tracking for move events without clicking
        )
        
        # Create visual feedback objects
        self.cursor_circle = PCircle(400, 300, 10, brushColor=QColor("#FF0000"))
        self.cursor_circle.set_isPen(False)
        
        self.click_indicator = PRectangle(350, 250, 100, 100, brushColor=QColor("#00FF00"))
        self.click_indicator.set_isPen(False)

        self.mouseLabel = PText(self.width/2, 50, "", brushColor=QColor("#FFFFFF"))
        
    def setup_objects(self):
        self.window.add_painter_object(self.cursor_circle)
        self.window.add_painter_object(self.click_indicator)
        self.window.add_painter_object(self.mouseLabel)
    
    def update(self):
        pass
    
    # --- Mouse Event Handlers ---
    
    def on_mouse_move(self, event):
        """Called when mouse moves (requires mouse_tracking=True)"""
        self.cursor_circle.x = event.pos().x()
        self.cursor_circle.y = event.pos().y()
        print(f"Mouse moved to: ({event.pos().x()}, {event.pos().y()})")
        self.mouseLabel.text = f"({event.pos().x()}, {event.pos().y()})"
    
    def on_mouse_press(self, event):
        """Called when a mouse button is pressed"""
        button = "Left" if event.button() == Qt.MouseButton.LeftButton else \
                 "Right" if event.button() == Qt.MouseButton.RightButton else "Middle"
        print(f"{button} mouse button pressed at ({event.pos().x()}, {event.pos().y()})")
        
        # Change color on press
        self.click_indicator.set_color(QColor("#FFFF00"), QColor("#FFFF00"))
    
    def on_mouse_release(self, event):
        """Called when a mouse button is released"""
        print(f"Mouse button released")
        
        # Reset color on release
        self.click_indicator.set_color(QColor("#00FF00"), QColor("#00FF00"))
    
    def on_mouse_double_click(self, event):
        """Called when mouse is double-clicked"""
        print(f"Mouse double-clicked at ({event.pos().x()}, {event.pos().y()})")
        self.click_indicator.set_color(QColor("#FF00FF"), QColor("#FF00FF"))
    
    def on_mouse_wheel(self, event):
        """Called when mouse wheel is scrolled"""
        delta = event.angleDelta().y()
        direction = "up" if delta > 0 else "down"
        print(f"Mouse wheel scrolled {direction} (delta: {delta})")
        
        # Change cursor circle size with scroll
        self.cursor_circle.r = max(5, min(50, self.cursor_circle.r + (1 if delta > 0 else -1)))
    
    def on_mouse_enter(self, event):
        """Called when mouse enters the window"""
        print("Mouse entered window")
        self.cursor_circle.set_color(QColor("#00FF00"), QColor("#00FF00"))
    
    def on_mouse_leave(self, event):
        """Called when mouse leaves the window"""
        print("Mouse left window")
        self.cursor_circle.set_color(QColor("#FF0000"), QColor("#FF0000"))
    
    # --- Keyboard Event Handlers ---
    
    def on_key_press(self, event):
        """Called when a key is pressed (ESC is handled automatically to close)"""
        key = event.text()
        print(f"Key pressed: {key if key else event.key()}")
        
        # Example: Change rectangle position with arrow keys
        if event.key() == Qt.Key.Key_Up:
            self.click_indicator.y -= 10
        elif event.key() == Qt.Key.Key_Down:
            self.click_indicator.y += 10
        elif event.key() == Qt.Key.Key_Left:
            self.click_indicator.x -= 10
        elif event.key() == Qt.Key.Key_Right:
            self.click_indicator.x += 10
    
    def on_key_release(self, event):
        """Called when a key is released"""
        print(f"Key released: {event.key()}")


if __name__ == "__main__":
    app = EventsDemoApp()
    app.run()

