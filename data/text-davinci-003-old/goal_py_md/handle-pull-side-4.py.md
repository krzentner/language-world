

Steps:
1. Put gripper near the handle
2. Grab the handle with the gripper
3. Pull up the handle

 
```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    # Move the gripper near the handle
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Grab the handle by closing the gripper around it
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("completely around the handle", close_gripper=True)
    # Now that the gripper is locked around the handle, pull up the handle
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")