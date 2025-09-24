# PyQtPaint
**This is still a work in progress, but basic functionality is present.**
A library of boilerplate code using the PyQt5 library. Used for creating a window to draw in and having an application and update thread. Also comes with some predefined objects to add to the window for drawing.

## Modules
* `PyQtPaint.app`:
Contains the `App` abstract class for running the window and updates to it.

* `PyQtPaint.form`:
Contains the `PainterWindow` class of which objects can be added and removed from it. These objects will be painted on every update call.

* `PyQtPaint.objects`:
Contains the `PainterObject` abstract class which descendants will have paint methods and other styling methods for customizing the object.

(Tests are currently of an older version)