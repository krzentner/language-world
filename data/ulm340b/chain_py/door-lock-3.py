
    # Steps:
    #  1. Put gripper above the door lock
    #  2. Drop gripper around door lock
    #  3. Turn the dial on the door lock
    # The gripper can't grab the door lock from the side.
    # Put the gripper above the door lock.
    if check("the robot's gripper is not vertically aligned with door lock"):
        robot.move("gripper above door lock")
    # As long as the gripper is aligned with the door lock, closing the gripper
    # should put the gripper around the door lock.
    if check("the robot's gripper is vertically aligned with door lock and the robot's gripper is open"):
        robot.put("gripper around door lock")
    # The gripper should now be closed around the dial on the door lock.
    # Turn the dial.
    if check("the robot's gripper is around door lock"):
        robot.turn("dial")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# door-lock: turn the dial on the door
def door_lock(robot):
    #