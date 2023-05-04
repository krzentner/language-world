
    # Steps:
    #  1. Put gripper above nail
    #  2. Start lowering gripper towards nail
    #  3. Start pushing nail into wood
    # If the gripper is not vertically aligned with the nail and the hammer,
    # put it there.
    if check("the robot's gripper is not vertically aligned with the hammer and the robot's gripper is not vertically aligned with nail"):
        robot.move_gripper("vertically aligned with the hammer")
    # If the gripper is vertically aligned with the nail but not near it,
    # start lowering the hammer towards the nail.
    # Because the nail can pop up a bit, it's okay if we end up below the nail.
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is not near the nail"):
        robot.move_gripper("near the nail")
    # If the gripper is hitting the nail, keep pushing down, in case the nail
    # isn't all the way into the wood yet.
    if check("the nail is below the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the hammer")

# place-red-in-green-cup: pick up the red block and place it in the green cup
def place_red_in_green_cup(robot):
    # Steps:
    #  1. Put gripper above the red block
    #  2. Drop gripper around red block
    #  3. Close gripper around red block
    #  4. Move red block above the green cup
    #  5. Open gripper to drop red block into green cup
    # First, put the gripper roughly above the red block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the red block"):
        robot.move_gripper("above the red block")
    # If the gripper isn't around the red block, put it around the red block.
    if check("the robot's gripper is not around red block and the robot's gripper is open"):
        robot.move_gripper("near the red block", close_gripper=True)
    # If the gripper is near the red block and open, maybe we can