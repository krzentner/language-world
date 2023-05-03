# Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # If the gripper is not vertically lined up with the door handle, we should
    # move the gripper near the door handle to start pushing
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.move("gripper to above door handle")
    # Once the gripper is around the door handle, we can start pushing the door
    # closed.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed to goal")