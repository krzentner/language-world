

### Task description

We will execute the following procedure:

- First, put the gripper above handle.
- If the handle is not vertically aligned with the gripper, move the gripper above handle.
- If the gripper is vertically aligned with handle, move the gripper near handle.

### Execution

```
> python
>>> from robot import Robot
>>> robot = Robot()
>>> robot.state()
robot at position [0.0 0.0 0.0] with gripper open
puck at position [1.0 1.0 0.0]
door handle at position [-1.0 1.0 0.0]
drawer handle at position [1.0 1.0 0.0]
window handle at position [0.0 -1.0 0.0]
button at position [1.0 -1.0 0.0]
peg at position [0.0 0.0 0.0]
target location at position [0.0 0.0 0.0]
handle at position [0.0 0.0 0.0]
>>> from program import *
>>> handle_press_side(robot)
> python
>>> from robot import Robot
>>> robot = Robot()
>>> robot.state()
robot at position [0.0 0.0 0.0] with gripper open
puck at position [1.0 1.0 0.0]
door handle at position [-1.0 1.0 0.0]
drawer handle at position [1.0 1.0 0.0]
window handle at position [0.0 -1.0 0.0]
button at position [1.0 -1.0 0.0]
peg at position [0.0 0.0 0.0]
target location at position [0.0 0.0 0.0]
handle at position [0.0 0.0 0.0]
>>> from program import *
>>> handle_press_side(robot)
>>> robot.state()
robot at position [0.0 0.0 0.0] with gripper open
puck at position [1.0 1.0 0.0]
door handle at position [-1.0 1.0 0.0]
drawer handle at position [1.0 1.0 0.0]
window handle at position [0.0 -1.0 0.0]
button at position [1.0 -1.0 0.0]
peg at position [0.0 0