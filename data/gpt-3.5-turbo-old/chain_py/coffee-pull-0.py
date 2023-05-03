# Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Lift the mug off the table
    #  4. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # If the gripper is not around the mug, grab it.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.grab("mug")
    # Once the mug is grabbed, lift it off the table.
    if check("the robot's gripper is around mug"):
        robot.lift("mug off the table")
    # Move the mug to the target location.
    if check("the mug is not at the target location"):
        robot.move("mug to target location")