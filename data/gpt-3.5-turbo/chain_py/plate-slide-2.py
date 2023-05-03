# Steps:
    #  1. Put gripper above the plate
    #  2. Push the gripper down on the plate
    #  3. Slide the plate into the target location
    # To slide the plate, the robot needs to push down on the plate and move the
    # gripper forward.
    # If the gripper is not aligned with the plate from above, move it above the
    # plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    # Once the gripper is above the plate, push down on it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not pushing down on the plate"):
        robot.push("down on the plate")
    # Once the gripper is pushing down on the plate, slide the plate forward
    # into the target location.
    if check("the robot's gripper is pushing down on the plate"):
        robot.slide("the plate to the goal")