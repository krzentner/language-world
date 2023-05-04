
    # Steps:
    #  1. Put the gripper below and in front of the ball
    #  2. Push the ball towards the target location
    # We need to keep the robot's gripper in front of the ball, because the ball
    # is round and will just roll out from under the gripper.
    if check("the robot's gripper is not in front of the soccer ball and the robot's gripper is not forward aligned with the soccer ball"):
        robot.move_gripper("in front of the soccer ball")
    # If the robot's gripper is in front of the ball but not aligned with it,
    # align it.
    if check("the robot's gripper is in front of the soccer ball"):
        robot.move_gripper("forward aligned with the soccer ball")
    # If the robot's gripper is in front of and aligned with the ball, we can
    # push it towards the target location.
    if check("the soccer ball is below the robot's gripper"):
        robot.move_gripper("in front of the target location")

# block-push: push the block to the target location
def block_push(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Push the block to the target location
    # First, we need to put the gripper above the block.
    if check("the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("above the block")
    # Now that the gripper is above the block, we can drop it around the block.
    if check("the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block and the robot's gripper is not near the block"):
        robot.move_gripper("above the block", close_gripper=True)
    # Finally, push the block to the target location by moving the gripper
    # there.
    if check("the robot's gripper is vertically aligned with the block"):
        robot.move_gripper("above the target location")

# button-press: push the button
def button_press(robot):
    # Steps:
   