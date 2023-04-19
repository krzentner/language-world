# Steps:
    # 1. Put gripper above hole
    # 2. Drop gripper around peg
    # 3. Lift peg out of the hole
    # 4. Move peg to goal
    # First, put the gripper above the hole by checking that the gripper is not already vertically aligned with the hole
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.place("gripper above hole")
    # Once the gripper is above the hole, drop it around the peg and grab the peg by closing the gripper
    if check("the robot's gripper is above hole and the robot's gripper is open"):
        robot.drop("gripper around peg")
        robot.close("gripper around peg")
    # The peg is now lifted out of the hole, and we can move it to the goal location
    if check("the robot's gripper is closed around peg"):
        robot.place("peg at goal")