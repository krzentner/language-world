
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# shelf-push: slide the block to the target location
def shelf_push(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Push gripper into top of block
    #  3. Slide block to goal
    # The robot can slide the block by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the block isn't below the gripper as seen from above, move the gripper
    # above the block.
    if check("the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # If the gripper is aligned with the block but not near it, move the gripper
    # down to the block to slide it.
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not near block"):
        robot.move_gripper("above the block", close_gripper=True)
    # If the gripper is near the block, we've probably trapped the block and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the block