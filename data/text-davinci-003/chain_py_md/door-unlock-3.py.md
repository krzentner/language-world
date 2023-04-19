

The program should follow these steps:

1. Put gripper above door handle
2. Drop gripper around door handle
3. Rotate the dial of the door handle

# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Rotate the dial of the door handle
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # Rotate the dial until the door unlocks.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.rotate("dial of door handle")