
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")

# block-push: slide the block to the target location
def block_push(robot):
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
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is