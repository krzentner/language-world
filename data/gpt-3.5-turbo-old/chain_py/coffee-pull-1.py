# Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Grab the handle of the mug with the gripper
    #  3. Pull the mug towards the target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not above the handle of the mug"):
        robot.place("gripper above mug handle")
    # If the gripper is not around the mug's handle and the gripper is open
    # move the gripper around the handle.
    if check("the robot's gripper is not around the handle of the mug and the robot's gripper is open"):
        robot.drop("gripper around the handle of the mug")
    # If the gripper is around the handle of the mug and the mug is not near
    # the target location, slide the mug towards the target location while
    # holding the handle with the gripper.
    if check("the robot's gripper is around the handle of the mug and the mug is not near the target location"):
        robot.pull("the mug towards the target location while holding the handle with the gripper")