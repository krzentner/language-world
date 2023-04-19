

The steps for the `box-close` task are as follows:
  1. Put gripper roughly above the box lid
  2. Grasp the lid with the gripper
  3. With the lid in the gripper, move the robot over the box
  4. Slowly lower the lid onto the box

```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper roughly above the box lid
    #  2. Grasp the lid with the gripper
    #  3. With the lid in the gripper, move the robot over the box
    #  4. Slowly lower the lid onto the box
    # First, put the gripper roughly above the box lid. 
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # If the gripper is above the box lid, try to grab it. 
    if check("the robot's gripper is above the box lid"):
        robot.grab("box lid")
    # If the box lid is in the gripper, move the robot over the box.
    if check("the box lid is in the robot's gripper"):
        robot.move("over the box")
    # With the lid in the gripper, slowly lower the lid onto the box.
    if check("the robot is above the box and the box lid is in the robot's gripper"):
        robot.slowly("lower the lid onto the box")
```