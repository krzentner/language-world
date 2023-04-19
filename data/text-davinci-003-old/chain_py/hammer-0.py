
    # Steps:
    #  1. Put gripper above nail head
    #  2. Drop gripper around nail head
    #  3. Pull up on the hammer to hit the nail
    # We need to put the gripper above the nail head before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with nail head"):
        robot.put("gripper above nail head")
    # Once the gripper is lined up above the nail head, we should be able to
    # grab the nail head by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with nail head and the robot's gripper is not around nail head"):
        robot.drop("gripper around nail head")
    # Once the gripper is around the nail head, we can just pull the hammer up
    # to hit the nail.
    if check("the robot's gripper is around nail head"):
        robot.pull("hammer up")