

Then, please write the code.
"""
def door_unlock(robot):
    # Steps:
    #  1. Put gripper on right side of the dial
    #  2. Turn the dial counterclockwise
    # Because this is "counterclockwise", we just need to turn the dial to the left.
    # First, put the gripper on right side of the dial
    if check("the robot's gripper is not on the right side of the dial and the robot's gripper is not around dial"):
        robot.put("gripper on the right side of the dial")
    # Now that the gripper is lined up, turn the dial to the left.
    if check("the robot's gripper is on the right side of the dial and the robot's gripper is not around dial"):
        robot.push("the dial to the left")


"""
```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper on right side of the dial
    #  2. Turn the dial counterclockwise
    # Because this is "counterclockwise", we just need to turn the dial to the left.
    # First, put the gripper on right side of the dial
    if check("the robot's gripper is not on the right side of the dial and the robot's gripper is not around dial"):
        robot.put("gripper on the right side of the dial")
    # Now that the gripper is lined up, turn the dial to the left.
    if check("the robot's gripper is on the right side of the dial and the robot's gripper is not around dial"):
        robot.push("the dial to the left")
```

Well done.

"""


"""
# Here are all the possible tasks the robot can do
# The robot can open drawers, windows, doors, press buttons, and slide pucks.
all_tasks = [
    "window-open",
    "button-press-side",
    "button-press-topdown",
    "reach",
    "pick-place",
    "drawer-open",
    "drawer-close",
    "window-close",
    "door-open",
    "door-unlock",
    "peg-insert-side",
    "push",
]

# Here's an example of an agent that can perform some of these tasks
agent = {