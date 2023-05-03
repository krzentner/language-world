

# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop the gripper around the handle of the hammer
    #  3. Move the hammer towards the nail
    #  4. Hammer the nail into place
    # First, move the gripper to a place above the hammer to get ready to grab 
    # it.
    if check("the robot's gripper is not vertically aligned the handle of the hammer"):
        robot.move_gripper("vertically aligned with the handle of the hammer")
    # Once the gripper is lined up above the handle, move the gripper around it
    # to grab it.
    if check("the robot's gripper is vertically aligned with the handle of the hammer and the robot's gripper is not closed around the handle"):
        robot.move_gripper("around the handle of the hammer",close_gripper=True)
    # Once the gripper has grabbed the handle, move the hammer near the nail.
    if check("the robot's gripper is closed around the handle of the hammer and the hammer is not near the nail"):
        robot.move_gripper("near the nail")
    # Finally, move the hammer down quickly to hammer  the nail into place.
    if check("the hammer is near the nail"):
        robot.move_gripper("down on the nail")