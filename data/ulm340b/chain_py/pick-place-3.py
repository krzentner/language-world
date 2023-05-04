
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Place puck in goal
    # First, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # If the gripper is near the puck, we've probably picked up the puck and can
    # just move to place it in the goal.
    if check("the robot's gripper is near the puck"):
        robot.place("the puck in the goal")

# pick-hold: pick up the puck and hold it somewhere
def pick_hold(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    # First, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # When the gripper is near the puck, we've probably picked it up and can just
    # hold it.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.hold("puck")

# stack: pick up the puck and stack it on top of the block
def stack(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #