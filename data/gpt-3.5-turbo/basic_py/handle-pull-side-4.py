    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper above handle")
    if check("handle is not to the left of the gripper and handle is not forward aligned with the gripper"):
        robot.grab("handle")
    if check("the grip is forward aligned with handle and handle is not vertically aligned with the slot"):
        robot.align("handle to slot")
    if check("the grip is vertically aligned with the slot"):
        robot.pull("handle up and towards the robot")