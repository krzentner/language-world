 
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper roughly above the door handle, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is roughly above the door handle, we should be able to
    # grab it by moving the gripper down around it.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.drop("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")
    
# door-close: push the door closed
# def door_close(robot): 
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door
    # handle.
    # We don't need to be careful about the direction, since the door is large and
    # we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")