# Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    #  4. Release the mug
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    # If the gripper is not around the mug, grab the mug.
    if check("the robot's gripper is not around mug"):
        robot.grab("mug")
    # If the gripper is holding the mug and not at the target location, move it
    # to the target location.
    if check("the robot's gripper is holding the mug and the mug is not at the target location"):
        robot.move("the mug to the target location")
    # If the gripper is holding the mug at the target location, release it.
    if check("the robot's gripper is holding the mug at the target location"):
        robot.release("mug")