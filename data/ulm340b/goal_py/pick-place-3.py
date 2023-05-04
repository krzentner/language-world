
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck
    #  3. Move to the target location with the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is aligned above the puck, we should be able to grab it
    # by moving the gripper down to it.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper is around the puck, we can move the gripper to the target
    # location while still holding the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("near the target location")

# pick-place-topdown: pick up the puck and hold it at the target location
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck
    #  3. Move gripper to target location with puck
    # First, move the gripper above the puck
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # When the gripper is above the puck we should be able to grab the puck by
    # closing the gripper around it
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper is around the puck we can move the gripper to the target
    # location while still holding the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("near the target location")

# pick-place-side: pick up the puck and hold it at the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck
    #  3. Move gripper to target location