

and end with the text:

```
robot.wrap("wrench around peg")
```

The program's flow should match the following example video, and use a number of intermediate states between the initial state and the final state.

<video controls loop width="50%">
    <source src="https://storage.googleapis.com/robot-learning-public-assets/robotic_assembly.mp4"
            type="video/mp4">
    Your browser does not support the video tag.
</video>
"""

#####################
# HELPER FUNCTIONS
#####################

import numpy as np


def check(condition):
    return bool(condition)


def put(obj1, obj2, position="above", alignment="vertical", orientation="no"):
    """Put obj1 position obj2 with alignment and orientation.
    Example:
        put("robot's gripper", "puck", "above", "vertical", "no")
    Args:
        obj1 (str): string describing the first object.
        obj2 (str): string describing the second object.
        position (str, optional): position of obj1 wrt obj2. Defaults to "above".
        alignment (str, optional): alignment of obj1 wrt obj2. Defaults to "vertical".
        orientation (str, optional): orientation of obj1 wrt obj2. Defaults to "no".
    Returns:
        str: description of action.
    """
    return f"put {obj1} {position} {obj2} with {alignment} alignment and {orientation} orientation"


def drop(obj1, obj2, alignment="forward", orientation="no"):
    """Drop obj1 to have alignment with obj2 with orientation.
    Example:
        drop("robot's gripper", "puck", "forward", "no")
    Args:
        obj1 (str): string describing the first object.
        obj2 (str): string describing the second object.
        alignment (str, optional): alignment of obj1 wrt obj2. Defaults to "forward".
        orientation (str, optional): orientation of obj1 wrt obj2. Defaults to "no".
    Returns:
        str: description of action.
    """
    return f"drop {obj1} to have {alignment} alignment with {obj2} with {orientation} orientation"


def grab(obj1, obj2, alignment="forward", orientation="no"):
    """Grab obj2 with obj1 with alignment and orientation.
    Example:
        grab("robot's gripper", "puck