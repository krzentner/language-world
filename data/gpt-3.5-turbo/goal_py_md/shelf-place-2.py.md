# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Lift block up
    #  5. Move gripper to target location
    #  6. Lower block down
    #  7. Open gripper to release block
    # First, put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("above the target location", open_gripper=False)
    # Move the gripper to the target location once the block has been lifted up.
    if check("the robot's gripper is above the target location and the block is in the gripper's grasp"):
        robot.move_gripper("almost vertically aligned with the target location", open_gripper=False)
    # Lower the block down once the gripper is above the target location.
    if check("the robot's gripper is almost vertically aligned with the target location and the block is in the gripper's grasp"):
        robot.move_gripper("near the target location", open_gripper=False)
    # Open the gripper to release the block at the target location.
    if check("the robot's gripper is near the target location and the block is in the gripper's grasp"):
        robot.move_gripper("near the target location", open_gripper=True)