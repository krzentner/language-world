# Steps:
    #  1. Put gripper above the peg
    #  2. Open the gripper
    #  3. Move gripper down around the base of the peg
    #  4. Close the gripper around the base of the peg
    #  5. Lift up the peg out of the hole
    #  6. Move the gripper to the target location
    #  7. Release the peg at the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Open the gripper.
    if check("the robot's gripper is not open"):
        robot.open("gripper")
    # Move the gripper down and around the base of the peg.
    if check("the gripper is not around the base of the peg"):
        robot.move("gripper around the base of the peg")
    # Close the gripper around the base of the peg.
    if check("the robot's gripper is around the base of the peg and the robot's gripper is open"):
        robot.close("gripper around the base of the peg")
    # Lift up the peg out of the hole.
    if check("the robot's gripper is holding the peg and is above the hole"):
        robot.lift("the peg out of the hole")
    # Move the gripper to the target location.
    if check("the robot's gripper is holding the peg and is not at the target location"):
        robot.move("gripper to the target location")
    # Release the peg at the target location.
    if check("the robot's gripper is holding the peg and is at the target location"):
        robot.release("peg at target location")