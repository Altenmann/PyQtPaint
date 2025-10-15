
# Testing the app functionality with a simple subclass of App

from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQtPaint import App, PLine
from math import sin, cos, pi
import random, time

class Branch:
    def __init__(self, x, y, theta, length, size):
        self.xEnd, self.yEnd = self.get_end(x, y, theta, length)
        self.theta = theta
        self.length = length
        self.size = size
        if theta > 2 * pi: theta -= 2 * pi
        elif theta < 0: theta += 2 * pi

        # Get a HSL color based on the angle of the branch
        color = QColor.fromHsl(int(theta * 180 / pi), 255, int(255/2))

        # PainterObject PLine (add this to the PainterWindow)
        self.line = PLine(x, y, self.xEnd, self.yEnd, penColor=color)
        self.line.set_line_width(size)
        self.line.set_line_cap(Qt.RoundCap)

    def get_end(self, x, y, theta, size):
        xEnd = x + cos(theta) * size
        yEnd = y + sin(theta) * size
        return xEnd, yEnd

# Example subclass of App
class TreeApp(App):

    def __init__(self):
        # Apply settings of the App
        # super().__init__(fullscreen=True, fps=5)
        # Use width and height instead of fullscreen
        super().__init__(width=700, height=700, fps=5)

        self.level = []
        self.branches = []
        self.levels = 10
        self.updates = 0

    # Implement abstract method that is called before the app starts updating
    def setup_objects(self):
        self.level = [Branch(self.width/2, self.height, 3*pi/2, 150, self.levels)]
        self.branches.extend(self.level)
        self.add_level()

    def add_level(self):
        # Add PLines that haven't been added yet
        self.window.add_painter_objects([branch.line for branch in self.level])

    # Implement abstract method that will be called on a background thread
    def update(self):
        if (self.updates+1) % self.levels == 0:
            time.sleep(2)
            # Remove all lines that were added to the window
            self.window.remove_painter_objects([branch.line for branch in self.branches])
            # Re-setup
            self.setup_objects()
            self.branches = []
            self.updates += 1
            return

        newLevel = []
        for branch in self.level:
            dTheta1 = random.random() * pi / 5 + pi / 20
            dTheta2 = random.random() * pi / 5 + pi / 20
            newLevel.append(
                Branch(
                    branch.xEnd, 
                    branch.yEnd, 
                    branch.theta + dTheta1, 
                    .9 * branch.length,
                    branch.size - 1
                )
            )
            newLevel.append(
                Branch(
                    branch.xEnd, 
                    branch.yEnd, 
                    branch.theta - dTheta2, 
                    .9 * branch.length,
                    branch.size - 1
                )
            )
        self.level = newLevel
        self.branches.extend(self.level)
        self.add_level()
        self.updates += 1


if __name__ == "__main__":
    # Initialize and run the App subclass
    app = TreeApp()
    app.run()