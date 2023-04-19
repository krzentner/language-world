

Steps to complete `coffee-pull`:
1. Put gripper above the mug
2. Drop gripper around mug
3. Close gripper around mug
4. Move mug to target location

# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to target location
    # Move the robot's gripper above the mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Once the mug is controlled by the gripper, move it to the target location.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("near the target location")