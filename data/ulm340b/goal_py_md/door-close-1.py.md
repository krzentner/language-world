

and complete the `def door_close(robot)` function.

The way that the robot moves its gripper depends on how you describe the way
that you want the gripper to move.

You can move the gripper by calling the function

```
move_gripper(description, close_gripper)
```

You can close the gripper by calling the function

```
move_gripper(description, close_gripper)
```

If the gripper is already closed, `robot.close_gripper()` will not change it.
"""

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door handle is
    # large and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("above the door handle")

######################################################################

#####################################
# End of Story
#####################################

print("")
print("")
print("Thanks for your help!")
[eod] [code]"""
Copyright (c) 2019 Uber Technologies, Inc.

Licensed under the Uber Non-Commercial License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at the root directory of this project. 

See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
import tensorflow_probability.python.layers as tfp_layers
import math

def create_mlp_model_nobn_wo_d(
        state_dim,
        action_dim,
        hidden_sizes=(256, 256),
        name="bc",
        is_training=True,
):
    """