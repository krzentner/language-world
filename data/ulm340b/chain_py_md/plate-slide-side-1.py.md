

As a hint, you can start with this program:

```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Move gripper over to plate
    #  3. Push plate sideways to target location
    # First, put the gripper above the plate, so that we don't bump it while
    # trying to slide it.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, move the gripper over to it.
    if check("the robot's gripper is above the plate"):
        robot.grab("plate")
    # We closed the gripper, and the plate is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the plate to the goal.
    if check("the robot's gripper is near plate"):
        robot.push("plate")
```

In the previous task, we made the robot do a sequence of actions by checking if the world
had a certain property and then performing an action to bring it closer to the goal
state.
"""

import pandas as pd
import sys

class Robot:
    def __init__(self):
        self.actions = {'grab': self.grab, 'close': self.close, 'drop': self.drop, 'push': self.push, 'slide': self.slide, 'insert': self.insert, 'align': self.align, 'pull': self.pull, 'move': self.move, 'push': self.push, 'place': self.place, 'put': self.put, 'reach': self.reach}
        self.gripper_opened = True

    def perform(self, action, object_position):
        getattr(self, action)(object_position)

    def grab(self, object_position):
        """
        Grabs the object (e.g. 'puck' or 'drawer handle') from position object_position.
        """
        pass

    def close(self, object_position):
        """
        Closes the gripper around the object (e.g. 'puck' or 'drawer handle') at position