```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    # 1. Put gripper above the box lid
    # 2. Grab the box lid with the gripper
    # 3. Line the box lid up with the box
    # 4. Lower the box lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid and closed, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # If the gripper is above the box, move it closer to the box.
    if check("the robot's gripper is above the box and not near the box"):
        robot.move_gripper("above the box", close_gripper=True)
    # If the box lid is near the box, lower it onto the box.
    if check("the robot's gripper is above the box and the box lid is near the box"):
        robot.move_gripper("on top of the box") 
```