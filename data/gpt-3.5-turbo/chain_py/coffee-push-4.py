# Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Grab the handle of the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not vertically aligned with the handle of the mug"):
        robot.put("gripper above the handle of the mug")
    # If the gripper is not around the mug, move it down to grab the handle.
    if check("the robot's gripper is vertically aligned with the handle of the mug and the robot's gripper is not around the handle"):
        robot.put("gripper around the handle of the mug")
    # If the gripper is around the handle of the mug, move the mug to the target location.
    if check("the robot's gripper is around the handle of the mug"):
        robot.move("the mug to the target location")