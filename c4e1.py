# c431_coordinate.py
# Jason Blunt

from graphics import *

def main():
    win = GraphWin("Coordinate System", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    origin = Circle(Point(0, 0), 2)
    origin.setFill("black")
    origin.draw(win)

    XAxis = Line(Point(-100, 0), Point(100, 0))
    XAxis.draw(win)

    yAxis = Line(Point(0, -100 ), Point(0, 100))
    yAxis.draw(win)

    for i in range(-100, 101, 10):
        tick = Line(Point(i, -5), Point(i, 5))
        tick.draw(win)

    for i in range(-100, 101, 10):
        tick2 = Line(Point(-5, i), Point(5, i))
        tick2.draw(win)

    originMarker = Text(Point(10, 8), "(0, 0)")
    originMarker.setSize(15)
    originMarker.draw(win)

main()
