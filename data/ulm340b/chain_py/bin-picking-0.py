
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Move gripper above the target bin
    #  5. Put cube into target bin
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # If the gripper is closed and near the cube, we must have successfully
    # grabbed it.
    # We can move the gripper above the target bin, then put the gripper and the
    # cube into the bin.
    if check("the robot's gripper is closed and the robot's gripper is near cube"):
        robot.move("gripper to above target bin")
        robot.put("cube into target bin")

# block-stack: pick up the block and put it on top of the stack
def block_stack(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move gripper above the block stack
    #  5. Put cube on top of block stack
    # First, put the gripper roughly above the block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.put("gripper around block")
    # If the gripper