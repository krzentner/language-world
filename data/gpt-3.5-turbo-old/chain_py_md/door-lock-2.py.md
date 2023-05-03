# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Turn the dial to lock the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # Once the gripper is around the handle, turn the dial in a clockwise direction
    if check("the robot's gripper is around door handle"):
        robot.turn("dial clockwise")