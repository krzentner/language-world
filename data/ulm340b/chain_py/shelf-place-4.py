
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move gripper up with block
    #  5. Slide block to goal
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # Once the block is above the gripper, we can pick it up and move it.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move("the gripper up with the block")
    # If we picked up the block, we can place it at the target location.
    if check("the robot's gripper is not above the block and the block is above the robot's gripper"):
        robot.slide("the block to goal")

# fridge-place-side: open the fridge, slide the fridge shelf to the side, place
# the block on the shelf, and close the fridge
def fridge_place_side(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move gripper up with block
    #  5. Slide block to goal
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    # If the gripper isn't around the