

Then, add the necessary code inside the function.

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to one side of the handle
    #  2. Move gripper horizontally to the other side of the handle
    #  3. Push down on handle until it clicks
    # First, put the gripper near one of the sides of the handle.
    if check("the robot's gripper is not near a side of the handle"):
        robot.put("gripper near the handle")
    # From the side, use the gripper to move horizontally to the other side.
    if check("the robot's gripper is not on the opposite side of the handle"):
        robot.move("gripper to other side of the handle")
    # From here, just push down on the handle until it clicks.
    if check("the robot's gripper is on the opposite side of the handle"):
        robot.push("down on handle until it clicks")
```