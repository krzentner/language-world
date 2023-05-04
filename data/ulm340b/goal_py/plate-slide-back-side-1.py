
    # Steps:
    #  1. Line the gripper up with the plate as seen from above
    #  2. Push the plate back sideways
    # Because we're pushing from the side, just line the robot's gripper up with
    # the plate.
    if check("the plate is not vertically aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")
    # Now that the gripper is lined up, just push the plate back sideways.
    if check("the plate is vertically aligned with the robot's gripper"):
        robot.move_gripper("above the plate")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Line the gripper up with the plate as seen from above
    #  2. Push the plate sideways
    # Because we're pushing from the side, just line the robot's gripper up with
    # the plate.
    if check("the plate is not vertically aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")
    # Now that the gripper is lined up, just push the plate sideways.
    if check("the plate is vertically aligned with the robot's gripper"):
        robot.move_gripper("left of the plate")

# push-back: push the small puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push puck to goal
    # The robot can slide the puck by moving the gripper above it and then
    # pushing it.
    if check("the puck is not vertically aligned with the robot's gripper and the robot's gripper is not near the puck"):
        robot.move_gripper("above the puck")
    # Once the robot's gripper is lined up with the puck, push the puck back.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not above the puck"):
        robot.move_gripper("vertically aligned with the puck")

# block-slide: slide the block into the target location
def block_slide(robot):
    # Steps:
    #