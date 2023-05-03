

Solution: 
```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to side of handle
    #  2. Push down on the handle
    # First, put the gripper to the side of the handle as seen from the front.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.put("gripper to side of handle")
    # If the the handle is aligned to the gripper, we can push the down the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle")
```