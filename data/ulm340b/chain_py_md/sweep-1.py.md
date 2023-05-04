

The program should be structured with `check` statements followed by `robot`
actions like the other demonstrations in this file.
If you prefer to avoid copy-and-pasting `check` statements, you can use the
following functions to check the relationships of interest.

To check if an object is `not_near`, `in_front`, `above`, `near`, or `not_above` the robot gripper,
you can use one of the following functions (where `object` is the name of the object of interest, e.g. `puck` or `cube`).

```
def not_near_gripper(object):
    return check("{} is not near the robot's gripper".format(object))
def in_front_gripper(object):
    return check("{} is in front of the robot's gripper".format(object))
def above_gripper(object):
    return check("{} is above the robot's gripper".format(object))
def near_gripper(object):
    return check("{} is near the robot's gripper".format(object))
def not_above_gripper(object):
    return check("{} is not above the robot's gripper".format(object))
```

And to check if the robot gripper is `not_above`, `open`, `near`, or `around` the object,
you can use one of the following functions (where `object` is the name of the object of interest, e.g. `puck` or `cube`).

```
def not_above_object(object):
    return check("the robot's gripper is not above {}".format(object))
def gripper_is_open(object):
    return check("the robot's gripper is open and is near {}".format(object))
def gripper_is_near(object):
    return check("the robot's gripper is near {}".format(object))
def gripper_is_around(object):
    return check("the robot's gripper is around {}".format(object))
```

You should complete the function below.
"""

import numpy as np

# Check functions
def not_near_gripper(object):
    return check("{} is not near the robot's gripper".format(object))
def in_front_gripper(object):
    return check("{} is in front of the robot's gripper".format(object))
def above_gripper(object):
    return check("{} is above the robot's gripper".format(