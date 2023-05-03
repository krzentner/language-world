

Steps:
1. Put gripper above hammer handle
2. Drop gripper around hammer handle
3. Move gripper up so that the bottom of the hammer is above the nail
4. Bring hammer down to hit the nail 

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Move gripper up so that the bottom of the hammer is above the nail
    #  4. Bring hammer down to hit the nail 
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not above hammer handle"):
        robot.move_gripper("above the hammer handle")
    # Once the gripper is above the hammer handle, drop it around the hammer
    # handle.
    if check("the robot's gripper is vertically aligned with the hammer handle"):
        robot.move_gripper("around the hammer handle")
    # If the gripper is around the hammer handle, move the gripper so that the
    # bottom of the hammer is above the nail.
    if check("the robot's gripper is around hammer handle"):
        robot.move_gripper("above the nail")
    # Finally, bring the hammer down to hit the nail.
    if check("the robot's gripper is above the nail"):
        robot.move_gripper("below the nail")