

The task `reach-pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?

The task `drawer-open-v1` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?

The task `drawer-close-v1` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?

The task `peg-insert-side-v1` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?

The task `window-open-v1` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?

The task `window-close-v1` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?

The task `button-press-topdown-v1` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?

The task `door-open-v1` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?
"""
        )
[eod] [code]#!/usr/bin/python3
"""This module implements a Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 