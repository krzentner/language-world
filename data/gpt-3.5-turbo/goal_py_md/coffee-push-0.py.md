# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # Check if the gripper is not above the mug
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above the mug")
    # Check if the gripper is not around the mug
    if check("the robot's gripper is above mug and the robot's gripper is not around the mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # Move the gripper to the target location with the mug
    if check("the robot's gripper is around the mug and the mug is below the robot's gripper"):
        robot.move_gripper("above the target location")