# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Move gripper to above the block
    #  2. Move gripper around the block
    #  3. Close the gripper around the block
    #  4. Move the block to the target location
    #  5. Drop the block
    
    # First, move the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    
    # Then, move the gripper around the block.
    if check("the robot's gripper is above the block and the robot's gripper is not around the block"):
        robot.move_gripper("around the block")
    
    # Close the gripper around the block.
    if check("the robot's gripper is around the block and the robot's gripper is open"):
        robot.move_gripper("around the block", close_gripper=True)
    
    # Move the block to the target location.
    if check("the robot's gripper is holding the block and the block is not at the target location"):
        robot.move_gripper("near the target location")
    
    # Finally, drop the block.
    if check("the robot's gripper is holding the block and the block is at the target location"):
        robot.release_gripper()