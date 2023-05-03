

Steps:
1. Put gripper below the lever.
2. Rotate the gripper around and grab the lever.
3. Move the lever up.

# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper below the lever
    #  2. Rotate the gripper around and grab the lever
    #  3. Move the lever up
    # First, put the gripper below the lever.
    if check("the robot's gripper is not below the lever"):
        robot.move_gripper("below the lever")
    # Since we can't rotate the robot's gripper from above, if the gripper is 
    # not angled to fit around the lever, move the gripper above the lever,
    # rotate the gripper, and then lower it back to the lever.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("above the lever")
        robot.move_gripper("rotate the gripper")
        robot.move_gripper("below the lever")
    # Once the gripper is around the lever, close the gripper.
    if check("the robot's gripper is around the lever and the robot's gripper is open"):
        robot.move_gripper("around the lever", close_gripper=True)
    # With the gripper closed, rotate the lever up.
    if check("the robot's gripper is around the lever and the robot's gripper is closed"):
        robot.move_gripper("above the lever")