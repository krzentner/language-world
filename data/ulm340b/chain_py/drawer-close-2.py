
    # Steps:
    #  1. Move gripper in front of drawer handle
    #  2. Push drawer shut
    # For this drawer, the robot's gripper won't be able to grab it, so just
    # push the front of it.
    if check("the robot's gripper is not in front of drawer handle"):
        robot.put("gripper in front of drawer handle")
    # Once the gripper is in front of the drawer handle, the robot should be
    # able to just push the drawer shut.
    if check("the robot's gripper is in front of drawer handle"):
        robot.push("drawer shut")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Move gripper in front of door handle
    #  2. Push door shut
    # Because this door doesn't have a handle on the opposite side of the
    # robot, the robot's gripper won't be able to grab it, so just push the
    # front of it.
    if check("the robot's gripper is not in front of door handle"):
        robot.put("gripper in front of door handle")
    # Once the gripper is in front of the door handle, the robot should be
    # able to just push the door shut.
    if check("the robot's gripper is in front of door handle"):
        robot.push("door shut")

# door-toggle: open or close the door
def door_toggle(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,