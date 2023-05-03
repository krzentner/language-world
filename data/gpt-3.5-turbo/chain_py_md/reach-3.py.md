# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper to above the target location
    #  2. Move gripper down to barely touch the target location
    # The goal of this task is to position the robot's gripper above the target
    # location so that it can later grab a small object there.
    # If the robot's gripper is not above the target location, move the gripper
    # there.
    if check("the robot's gripper is not above the target location"):
        robot.move("the gripper to above the target location")
    # If the gripper is above the target location but still needs to move down,
    # move it down so that it just barely touches the surface where the object
    # is located.
    if check("the robot's gripper is above but not touching the target location"):
        robot.move("the gripper down to barely touch the target location")