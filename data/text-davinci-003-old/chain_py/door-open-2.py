
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper up so that it's lined up with the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up enough, just close it around the door handle so
    # that the inside of the gripper is now around the handle.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.drop("gripper around door handle")
    # As long as the gripper is still around the door handle, keep pulling the
    # door open.
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")