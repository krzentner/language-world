# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    # If the gripper is not around the mug and is open, put the gripper around
    # the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and is closed, we've grabbed the mug. Move
    # it to the target location.
    if check("the robot's gripper is near the mug and the robot's gripper is closed"):
        robot.slide("mug to the target location")