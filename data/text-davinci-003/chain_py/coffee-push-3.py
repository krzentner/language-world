
    # Steps:
    #  1. Put the gripper above the mug
    #  2. Close the gripper
    #  3. Move it to the target location
    # If the gripper isn't above the mug, move it directly above the mug
    if check("the gripper is not above the mug"):
        robot.put("gripper above the mug")
    # If the gripper is above the mug and it's open, close the gripper
    if check("the gripper is above the mug and the gripper is open"):
        robot.close("gripper")
    # If the gripper is closed, move it to the goal
    if check("the gripper is above the mug and the gripper is closed"):
        robot.move("mug to target location")