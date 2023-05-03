# Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Grab mug handle
    #  4. Pull mug towards target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not above the mug handle"):
        robot.place("gripper above mug handle")
    # If the gripper isn't around the handle of the mug, drop it around the mug handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    # If the gripper is around the handle of the mug but not grabbed it, grab it by closing the gripper.
    if check("the robot's gripper is around mug handle and the robot's gripper is open"):
        robot.grab("mug handle")
    # Once the mug handle is grabbed, start pulling it towards the target location.
    if check("the mug handle is grabbed"):
        robot.pull("mug towards goal location")