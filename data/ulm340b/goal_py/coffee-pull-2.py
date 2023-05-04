
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Pull mug to goal
    # First, put the gripper above mug
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.move_gripper("above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug"):
        robot.move_gripper("above mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above mug"):
        robot.move_gripper("around mug")

# block-pick-place: pick up the block and hold it at the target location
def block_pick_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("vertically aligned with block")
    # If the gripper is above the block, we need to drop it down around the
    # block.
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is above the block"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above the block"):
        robot.move_gripper("horizontally aligned with block")

# door-open-pull: pull the door open to the left
def door_open_pull(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
