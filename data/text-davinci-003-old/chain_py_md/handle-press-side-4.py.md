

Steps:
 1. Put gripper left of the handle
 2. Push down on the handle
 
 
```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Push down on the handle
    # First, align the gripper to the left of the handle from the side.
    if check("the robot's gripper is not left of the handle"):
        robot.put("gripper left of handle")
    # Once the robot's gripper is left of the handle, press it down.
    if check("the robot's gripper is left of the handle"):
        robot.push("down on handle")
```