
    # Steps:
    #  1. Line up gripper as seen from above
    #  2. Grab peg with gripper
    #  3. Move the wrench around the peg
    # Line up the gripper as seen from above.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # Grab the peg with the gripper.
    if check("peg is not left of the robot's gripper and the robot's gripper is not near the peg"):
        robot.grab("peg")
    # Move the wrench around the peg
    if check("the gripper is forward aligned with peg and the wrench is not around the peg"):
        robot.place("wrench around peg")