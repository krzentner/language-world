# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Open the gripper
    # 3. Slide the jaws of the gripper around the peg
    # 4. Close the gripper around the peg
    # 5. Lift the wrench off the table
    # 6. Slide the wrench onto the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the gripper isn't open, open the gripper to prepare for grabbing the peg.
    if check("the robot's gripper is not open"):
        robot.drop("gripper open")
    # If the jaws of the gripper are not around the peg, slide the jaws around the peg.
    if check("the robot's gripper is open and the peg is not between the jaws of the gripper"):
        robot.grab("peg with gripper")
    # If the jaws of the gripper are around the peg, close the gripper to hold the peg.
    if check("the peg is between the jaws of the gripper and the gripper is open"):
        robot.close("gripper around peg")
    # Now lift the wrench off the table with the peg attached.
    if check("the gripper is closed around the peg and is near the surface of the table"):
        robot.lift("wrench off table with peg attached")
    # Move the wrench to the peg and slide it onto the peg.
    if check("the gripper is holding the wrench above the peg"):
        robot.slide("the wrench onto the peg")