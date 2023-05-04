
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # If the robot's gripper is not vertically aligned with the door handle,
    # move it above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # If the robot's gripper is lined up with the door handle, move it around
    # the door handle.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not near door handle"):
        robot.grab("door handle")
    # If the robot's gripper is near the door handle, pull the door open.
    if check("the robot's gripper is near door handle"):
        robot.pull("door open")

# door-close: push the door close
def door_close(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Push door closed
    # If the robot's gripper is not aligned with the door handle as seen from in
    # front, move it above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # If the robot's gripper is lined up with the door handle as seen from in
    # front, push the door closed.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# pick-reach: move the puck to the goal
def pick_reach(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the