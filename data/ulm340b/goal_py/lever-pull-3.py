
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever up
    # We need to put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # Once the gripper is lined up above the lever, we should be able to grab
    # the lever by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, we can rotate the lever up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("forward aligned with the lever")

# lever-push: rotate the lever down
def lever_push(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever down
    # We need to put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # Once the gripper is lined up above the lever, we should be able to grab
    # the lever by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, we can rotate the lever down.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("vertically aligned with the lever")

# push-back: push the block to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Push block into goal
    # Push blocks forward with the front of the gripper, not the sides.