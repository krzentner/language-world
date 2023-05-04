
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Slide the puck to the target
    # First, put the gripper above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck, push it along.
    if check("the robot's gripper is around the puck and the puck is not aligned with target location"):
        robot.move_gripper("aligned with target location")

# slide-drawer: open the drawer
def slide_drawer(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper above the drawer handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the drawer handle"):
        robot.move_gripper("above the drawer handle")
    # If the gripper isn't around the drawer handle, put it around the drawer
    # handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    # If the gripper is around the drawer handle, push it along.
    if check("the robot's gripper is around the drawer handle and the drawer handle is not aligned with the target location"):
        robot.move_gripper("aligned with target location")

# turn-switch-topdown: push the switch from above
def turn_switch_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the switch from the top
   