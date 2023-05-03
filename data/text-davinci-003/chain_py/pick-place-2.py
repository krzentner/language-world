
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move gripper to target
    #  4. Place puck at target
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # As long as the gripper is still mostly above the puck, close it.
    if check("the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.put("gripper around puck")
    # If the gripper is now around the puck and the gripper is not near the
    # target, move the gripper to the target.
    if check("the robot's gripper is around the puck and the robot's gripper is not near the target"):
        robot.move("gripper toward the target")
    # If the gripper is now near the target, put the puck down.
    if check("the robot's gripper is near the target"):
        robot.put("puck down at target")