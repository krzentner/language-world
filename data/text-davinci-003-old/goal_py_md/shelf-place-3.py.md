

The robot should pick up the block and place it at the target location.

Steps: 
1. Put gripper above block 
2. Drop gripper around block 
3. Close gripper around block 
4. Move block to target location 

# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to target location
    
    # First, put the gripper roughly above the block so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, close the gripper to grab the
    # block.
    if check("the robot's gripper is near the block and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # Once the block is in the gripper, move the block to the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location")