
    # Steps:
    #  1. Put gripper above the lever handle
    #  2. Drop gripper around lever handle
    #  3. Pull up the lever handle
    # First, put the gripper roughly above the lever handle.
    # We don't need to line up the gripper too carefully because we're just
    # putting the robot's gripper above it.
    if check("the robot's gripper is not above lever handle"):
        robot.put("gripper above lever handle")
    # As long as the gripper is above the lever handle, we can just close the
    # gripper to grab the lever handle.
    if check("the robot's gripper is above lever handle and the robot's gripper is open"):
        robot.grab("lever handle")
    # If the gripper is around the lever handle, we can rotate it up.
    if check("the robot's gripper is around lever handle and lever handle is below the robot's gripper"):
        robot.turn("lever up")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper below door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # First, put the gripper roughly below the door handle.
    # We don't need to line up the gripper too carefully because we're just
    # putting the robot's gripper below it.
    if check("the robot's gripper is not below door handle"):
        robot.put("gripper below door handle")
    # As long as the gripper is below the door handle, we can just close the
    # gripper to grab the door handle.
    if check("the robot's gripper is below door handle and the robot's gripper is open"):
        robot.grab("door handle")
    # If the gripper is around the door handle, we can push it closed.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# valve-open: turn the valve open
def valve_open(robot):
    # Steps:
    #  1. Put gripper above the valve handle
    #  2. Drop grip