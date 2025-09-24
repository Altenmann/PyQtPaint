
# Testing the app functionality with a simple fullscreen app

from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQtPaint.app import App
from PyQtPaint.objects import PLine
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
        color = QColor.fromHsl(int(theta * 180 / pi), 255, int(255/2))
        self.line = PLine(x, y, self.xEnd, self.yEnd, penColor=color)
        self.line.set_line_width(size)
        self.line.set_line_cap(Qt.RoundCap)

    def get_end(self, x, y, theta, size):
        xEnd = x + cos(theta) * size
        yEnd = y + sin(theta) * size
        return xEnd, yEnd

class TreeApp(App):

    def __init__(self):
        super().__init__(fullscreen=True, fps=5)

        self.level = []
        self.branches = []
        self.levels = 10
        self.updates = 0

    def setup_objects(self):
        self.width, self.height = self.window.width(), self.window.height()
        self.level = [Branch(self.width/2, self.height, 3*pi/2, 150, self.levels)]
        self.branches.extend(self.level)
        self.add_level()

    def add_level(self):
        self.window.add_painter_objects([branch.line for branch in self.level])

    def update(self):
        if (self.updates+1) % self.levels == 0:
            time.sleep(2)
            self.window.remove_painter_objects([branch.line for branch in self.branches])
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
    app = TreeApp()
    app.run()