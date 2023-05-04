
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # First, put the gripper roughly around the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # Now, since the gripper is near the drawer, we can pull it open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# pick-hold: pick up the puck and keep holding it
def pick_hold(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# pick-insert-side: pick up the puck and insert it into the hole from the side
def pick_insert_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the hole
    #  4. Slide the puck sideways into the hole
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the puck becomes left of the gripper, go back to putting the gripper
    # above the puck.
    # Because the puck is a long object, check if the