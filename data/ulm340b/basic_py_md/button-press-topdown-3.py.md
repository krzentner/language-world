

Your program should be a series of `if` checks like the previous examples.

Here is some information about the robot:

- The robot's gripper has a left and right finger and closes like a pinch.
- The robot's arm can move up, down, left, right, and in-between directions.

To complete this HIT please write a program in the text box below that will accomplish the task of 'button-press-topdown'.

Your program should be in the form:

```
# ...
def ...(robot):
    if ...:
        ...
```
"""

robot_tasks = {
    "push": "slide the puck to the target location",
    "reach": "reach to the target location",
    "window-close": "slide the window closed to the right",
    "peg-insert-side": "grab the peg and insert it into the hole from the side",
    "drawer-open": "pull the drawer open",
    "window-open": "slide the window open to the left",
    "pick-place": "pick up the puck and hold it at the target location",
    "drawer-close": "push the drawer close",
    "door-open": "pull the door open",
    "button-press-topdown": "push the button down from above",
}

robot_task_examples = {
    "push": "def push(robot):\n    if check(\"the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck\"):\n        robot.put(\"the gripper above the puck\")\n    if check(\"the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck\"):\n        robot.push(\"the gripper into the puck\")\n    if check(\"the robot's gripper is near the puck and the puck is below the robot's gripper\"):\n        robot.slide(\"the puck to the goal\")",
    "reach": "def reach(robot):\n    if check(\"the robot's gripper is not near reach target\"):\n        robot.reach(\"to goal\")",
    "window-close": "def window_close(robot):\n    if check(\"the window handle is right of the robot's gripper and the robot's gripper is not near the window handle\"):\n        robot.move(\"gripper to left of window handle\")\n    if check(\"the robot's gripper is near the window handle\"):\n       