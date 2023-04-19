

# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps: 
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper
    #  4. Move mug to the target location
    # First put the gripper roughly above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug")

    # If the gripper is not around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
        
    # If the gripper is near the mug and open, we can grab it by closing the
    # gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

    # If the mug isn't lined up as seen from in front of the target, move the
    # gripper to line it up.
    if check("the mug is not forward aligned with the target location"):
        robot.move_gripper("forward aligned with the target location")
        
    # Finally, move the mug towards the target location.
    if check("the mug is forward aligned with target location"):
        robot.move_gripper("near the target location")