# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Close gripper around hammer handle
    #  4. Put gripper above nail
    #  5. Drop gripper around nail
    #  6. Close gripper around nail
    #  7. Hit nail with hammer
    # First, put the gripper roughly above the hammer handle.
    if check("the robot's gripper is not above the hammer handle"):
        robot.place("gripper above hammer handle")
    # If the gripper isn't around the hammer handle, put it around the handle.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    # If the gripper is near the hammer handle and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near hammer handle and the robot's gripper is open"):
        robot.close("gripper around hammer handle")
    # Next, put the gripper above the nail.
    if check("the robot's gripper is not above the nail"):
        robot.place("gripper above nail")
    # If the gripper isn't around the nail, put it around the nail.
    if check("the robot's gripper is not around nail and the robot's gripper is closed"):
        robot.drop("gripper around nail")
    # If the gripper is near the nail and closed, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near nail and the robot's gripper is closed"):
        robot.close("gripper around nail")
    # Finally, hit the nail with the hammer.
    if check("the robot's gripper is around the nail and the robot's gripper is around the hammer handle"):
        robot.hit("the nail with the hammer")