
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull the drawer open
    # First, put the gripper mostly above the drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("above the drawer handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper near door handle
    #  2. Push the door closed
    #  3. Open gripper
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("left of the door handle")

# pick-place-side: pick up the puck and place it at the side of the target
# location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close gripper around the puck
    #  4. Move puck sideways to target
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper isn't around the puck, put it