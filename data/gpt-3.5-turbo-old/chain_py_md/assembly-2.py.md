# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper above the peg
    #  4. Move gripper so that the wrench is around the peg
    #  5. Release the gripper to let go of the wrench
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in the gripper, try grabbing the wrench.
    if check("the wrench is not in the robot's gripper"):
        robot.grab("wrench")
    # Move the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # Move the gripper so that the wrench is around the peg.
    if check("the wrench is not around the peg"):
        robot.move("gripper so that the wrench is around the peg")
    # Release the gripper.
    if check("the wrench is around the peg"):
        robot.drop("gripper")