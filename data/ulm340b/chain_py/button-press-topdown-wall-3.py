
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, put the gripper above the button, so that it can be pushed down.
    # Since there's a wall, we also need to push the gripper forward to push the
    # button down.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    # Since the wall is there, also push the gripper forward.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-close-wall: push the drawer closed with a short wall in the way
def drawer_close_wall(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # First, put the gripper near the drawer handle, so that we can grab it and
    # push it.
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # Now that the gripper is lined up, just push the drawer closed.
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")

# door-close: close the door by pushing it closed
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is left of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the door handle is left of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move("gripper to right of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door close now by moving the gripper right.
    if check("the robot's gripper is near the door handle"):
        robot.