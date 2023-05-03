# Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper into hole and grab peg
    #  3. Pull peg out of hole
    #  4. Move peg to goal
    # First, put the gripper above the hole where the peg is located.
    if check("the robot's gripper is not above the hole"):
        robot.put("gripper above hole")
    # If the gripper is above the hole but not inside it, put it inside and grab the peg.
    if check("the robot's gripper is above hole and the robot's gripper is open"):
        robot.grab("peg inside hole")
    # Once the gripper is holding the peg inside the hole, pull the peg out of the hole.
    if check("the peg is inside the gripper and the gripper is not vertically aligned with the goal"):
        robot.pull("peg out of hole")
    # Move the peg to the goal location.
    if check("the grip is holding the peg and vertically aligned with the goal"):
        robot.place("peg at goal")