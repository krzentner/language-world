
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate back
    # We have to line the gripper up with the plate from the front before pushing
    # it back.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.put("gripper in front of plate")
    # Once the gripper is lined up with the plate, slide the plate back.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.slide("plate back")