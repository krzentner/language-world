
    # Steps:
    #  1. Put gripper above handle of wrench
    #  2. Move gripper towards peg
    #  3. Grab handle of wrench
    #  4. Pull wrench off the peg
    # First, put the gripper above the handle of the wrench.
    if check("the robot's gripper is not above handle of wrench"):
        robot.put("gripper above handle of wrench")
    # If the handle of the wrench is above the gripper, we should move the
    # gripper towards the peg to grab it.
    if check("the handle of the wrench is above the robot's gripper and the robot's gripper is open"):
        robot.move("gripper towards peg")
    # If the handle of the wrench is below the gripper and the gripper is open,
    # try to grab it.
    if check("the handle of the wrench is below the robot's gripper and the robot's gripper is open"):
        robot.grab("handle of wrench")
    # If our gripper is below the handle of the wrench and the gripper is closed,
    # pull the wrench off the peg.
    if check("the robot's gripper is below the handle of the wrench and the robot's gripper is closed"):
        robot.pull("wrench off peg")