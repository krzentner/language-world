

The robot should grab the mug and then move it to the target location.

# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to target location
    # First, put the gripper roughly above the mug, so we don't bump it while grabbing it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is around the mug and it's open, close the gripper to grab it.
    if check("the robot's gripper is around the mug and the robot's gripper is open"):
        robot.move_gripper("above the mug", close_gripper=True)
    # If the mug is now securely held, move it to the target location.
    if check("the robot's gripper is around the mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")