# Steps:
    #  1. Put gripper above the puck
    #  2. Close gripper to grab the puck
    #  3. Move gripper to the target location
    #  4. Open gripper to release the puck
    # First, move the gripper to be above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, close it to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the gripper is open"):
        robot.grab("puck")
    # Once the gripper has the puck, move it to the target location.
    if check("the gripper is holding the puck and the robot's gripper is not at target location"):
        robot.move("gripper to target location")
    # Once the gripper is at the target location, release the puck by opening
    # the gripper.
    if check("the gripper is at the target location holding the puck"):
        robot.release("puck")