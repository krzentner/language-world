
    # Steps:
    #  1. Move the gripper above the handle of the coffee mug
    #  2. Line up the gripper with the handle of the coffee mug
    #  3. Put the gripper around the handle of the coffee mug
    #  4. Close the gripper around the handle of the coffee mug
    #  5. Pull the mug to the target location
    # First, put the robot's gripper above the handle of the coffee mug.
    if check("the robot's gripper is not above the handle of the coffee mug"):
        robot.move_gripper("above the handle of the coffee mug")
    # If the handle is still ahead of the gripper, we need to continue lining up
    # the gripper with it.
    if check("the robot's gripper is above the handle of the coffee mug and the coffee mug's handle is not right of the robot's gripper"):
        robot.move_gripper("right of the handle of the coffee mug")
    # If the handle is right of the gripper, it should be lined up with it.
    # Move the gripper closer to grab it.
    if check("the coffee mug's handle is right of the robot's gripper"):
        robot.move_gripper("near the handle of the coffee mug", close_gripper=True)
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the handle of the coffee mug and the coffee mug's handle is right of the robot's gripper"):
        robot.move_gripper("near the target location")

# slider-pull: grab the slider and pull it to the target location
def slider_pull(robot):
    # Steps:
    #  1. Move the gripper above the slider
    #  2. Line up the gripper with the slider
    #  3. Put the gripper around the slider
    #  4. Close the gripper around the slider
    #  5. Pull the slider to the target location
    # First, put the robot's gripper above the slider.
    if check("the robot's gripper is not above the slider"):
        robot.move_gripper("above the slider")
    # If the slider