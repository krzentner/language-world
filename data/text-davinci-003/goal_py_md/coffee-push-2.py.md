

Steps:
  1. Put gripper above mug
  2. Grab mug with the gripper
  3. Move mug to the target location

# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab mug with the gripper
    #  3. Move mug to the target location
    # First, move the gripper above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug")
    # If the gripper is above the mug, but not around it, put the gripper
    # around the mug.
    if check("the robot's gripper is one above mug and the robot's gripper is not around mug"):
        robot.move_gripper("around mug", close_gripper=True)
    # Once the gripper is around the mug, we can start to move it to the target
    # location.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("near the target location")