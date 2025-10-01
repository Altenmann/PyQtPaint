# Event Handling Guide

## Overview
Event handling in PyQtPaint is now streamlined and intuitive. You can override event methods directly in your `App` subclass without needing separate handler classes.

## Quick Comparison

### Before (Old Way) ❌
```python
from PyQtPaint import App, MouseHandler
import types

mouseHandler = MouseHandler(True)

class MyApp(App):
    def __init__(self):
        super().__init__(mouse_handler=mouseHandler)
        self.setup_events()
    
    def setup_events(self):
        def move(handler, event):
            # Handle mouse move
            pass
        mouseHandler.move = types.MethodType(move, mouseHandler)
```

### After (New Way) ✅
```python
from PyQtPaint import App

class MyApp(App):
    def __init__(self):
        super().__init__(mouse_tracking=True)
    
    def on_mouse_move(self, event):
        # Handle mouse move - that's it!
        pass
```

## Available Event Methods

### Mouse Events
Override these methods in your `App` subclass:

- `on_mouse_press(event)` - Mouse button pressed
- `on_mouse_release(event)` - Mouse button released
- `on_mouse_double_click(event)` - Mouse double-clicked
- `on_mouse_move(event)` - Mouse moved (requires `mouse_tracking=True`)
- `on_mouse_enter(event)` - Mouse entered window
- `on_mouse_leave(event)` - Mouse left window
- `on_mouse_wheel(event)` - Mouse wheel scrolled

### Keyboard Events
Override these methods in your `App` subclass:

- `on_key_press(event)` - Key pressed (ESC automatically closes window)
- `on_key_release(event)` - Key released

## Configuration

### Mouse Tracking
To receive `on_mouse_move` events without clicking, enable mouse tracking:

```python
super().__init__(mouse_tracking=True)
```

### Custom Cursor
```python
from PyQt5.QtCore import Qt

self.window.setCursor(Qt.CursorShape.BlankCursor)  # Hide cursor
self.window.setCursor(Qt.CursorShape.CrossCursor)  # Crosshair
```

## Complete Example

```python
from PyQtPaint import App, PCircle
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class MyApp(App):
    def __init__(self):
        super().__init__(
            title='My App',
            width=800, height=600,
            mouse_tracking=True
        )
        self.circle = PCircle(400, 300, 20, brushColor=QColor("#FF0000"))
    
    def setup_objects(self):
        self.window.add_painter_object(self.circle)
    
    def update(self):
        pass  # Called automatically at self.fps rate
    
    def on_mouse_move(self, event):
        self.circle.x = event.pos().x()
        self.circle.y = event.pos().y()
    
    def on_key_press(self, event):
        if event.key() == Qt.Key.Key_Space:
            # Change circle color on spacebar
            self.circle.set_color(QColor("#00FF00"), QColor("#00FF00"))

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

## Migration Guide

If you have existing code using the old `MouseHandler` and `KeyHandler` classes:

1. Remove the handler class imports: `from PyQtPaint import MouseHandler, KeyHandler`
2. Remove handler instantiation: `mouseHandler = MouseHandler(True)`
3. Replace `mouse_handler=mouseHandler` with `mouse_tracking=True` (if needed)
4. Remove the `setup_events()` method
5. Convert handler methods to `on_*` methods in your App class

Example migration:
```python
# Old
def setup_events(self):
    def move(handler, event):
        self.circle.x = event.pos().x()
    mouseHandler.move = types.MethodType(move, mouseHandler)

# New - just override the method!
def on_mouse_move(self, event):
    self.circle.x = event.pos().x()
```

## Advanced Usage

You can also use `PainterWindow` directly and override its event methods:

```python
from PyQtPaint import PainterWindow

class CustomWindow(PainterWindow):
    def on_mouse_press(self, event):
        print("Custom window clicked!")

# Use with App
app = QApplication(sys.argv)
window = CustomWindow()
window.show()
sys.exit(app.exec_())
```

