
    # Steps:
    #  1. Put gripper above door lock handle
    #  2. Drop gripper around door lock handle
    #  3. Turn the handle clockwise
    # First, put the gripper above the door lock handle.
    if check("the robot's gripper is not vertically aligned with door lock handle"):
        robot.put("gripper above door lock handle")
    # Once the gripper is lined up above the door lock handle, we should be able
    # to grab the door lock handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door lock handle and the robot's gripper is not around door lock handle"):
        robot.put("gripper around door lock handle")
    # Once the gripper is around the door lock handle, we can just turn it
    # clockwise.
    if check("the robot's gripper is around door lock handle"):
        robot.turn("handle clockwise")