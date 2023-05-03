# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # The robot can slide the mug by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the mug isn't below the gripper as seen from above, move the gripper
    # above the mug.
    if check("the robot's gripper is not above the mug and the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the gripper is aligned with the mug but not near it, move the gripper
    # down to the mug to grab it.
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not near the mug"):
        robot.move_gripper("above the mug", close_gripper=True)
    # If the gripper is near the mug, we've probably trapped the mug and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the mug.
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.move_gripper("above the target location")