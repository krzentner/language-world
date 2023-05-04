
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug", open_gripper=True)
    # If the mug isn't left of the gripper, go back to putting the gripper
    # above the mug.
    # Because the mug is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the mug is not left of the robot's gripper and the mug is not horizontally aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the mug")
    # As long the gripper is still mostly around the mug and the mug isn't at
    # the target location, move the mug to the target location.
    if check("the mug is horizontally aligned with the robot's gripper"):
        robot.move_gripper("near the mug")

# coffee-pull: grab the mug and move it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug", open_gripper=True)
    # If the mug isn't left of the gripper, go back to putting the gripper
    # above the mug.
    # Because the mug is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the mug is not left of the robot's gripper and the mug is not horizontally aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the mug")
    # As long the gripper is still mostly around the mug and the mug isn't at
    # the target location, move the mug to the target location.
    if