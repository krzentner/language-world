
    # Steps:
    #  1. Put gripper above wrench
    #  2. Push gripper into the wrench
    #  3. Pull wrench off peg
    # If the grip handle is not above the wrench, move the gripper above the
    # wrench.
    if check("the robot's gripper is not above wrench"):
        robot.move("gripper above wrench")
    # If the gripper is above the wrench, we can move the wrench by pushing it
    # downwards into the wrench, then pulling the wrench off the peg.
    if check("the robot's gripper is above wrench"):
        robot.push("gripper into wrench")
    if check("the robot's gripper is below wrench"):
        robot.pull("wrench off peg")