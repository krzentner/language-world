# Steps:
    #  1. Put gripper near handle of mug
    #  2. Grab the handle
    #  3. Lift the mug and move it to the target location
    # First, put the gripper near the handle of the mug.
    if check("the robot's gripper is not near the handle of the mug"):
        robot.move("gripper near handle of mug")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle of mug and the robot's gripper is open"):
        robot.drop("gripper around handle of mug")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near handle of mug and the robot's gripper is open"):
        robot.close("gripper around handle of mug")
    # We closed the gripper and the mug is lifted, move the mug to the target location
    # Try moving mug forwards first as may be obstructed by other objects on table
    if check("the mug is not at the target location"):
        robot.move("mug forwards to goal")
    # Else move mug sideways
    if check("the mug is not at the target location"):
        robot.move("mug sideways to goal")