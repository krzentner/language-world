# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the handle of the mug.
    #  2. Grab the mug by enclosing the gripper around the mug's handle.
    #  3. Pull the mug towards the target location.
    # Before grabbing the mug's handle, move the gripper near it.
    if check("the robot's gripper is not near the handle of the mug"):
        robot.move("gripper above the handle of the mug")
    # If the gripper is near the handle, grab the mug's handle by enclosing
    # the gripper around it.
    if check("the robot's gripper is near the handle of the mug and the robot's gripper is open"):
        robot.enclose("the gripper around the handle of the mug")
    # If the gripper has grabbed the handle, move the mug towards the target location.
    # Keep moving the mug until it's at the target location.
    if check("the robot's gripper is around the handle of the mug"):
        while check("the mug is not at the target location"):
            robot.pull("the mug towards the target location")