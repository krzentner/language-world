

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper to target location
    #  2. Drop gripper around the target
    #  3. Close gripper around the target
    # First, move the gripper near the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    # Once the gripper is near the target, close the gripper around the target.
    if check("the robot's gripper is near the target"):
        robot.put("gripper around the target")
    # If the target is close enough to the gripper and the gripper is open,
    # close the gripper around the target.
    if check("the robot's gripper is near the target and the robot's gripper is open"):
        robot.close("gripper around the target")