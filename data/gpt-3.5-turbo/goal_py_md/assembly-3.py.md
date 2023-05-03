# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line up the wrench with the peg
    #  4. Move the gripper around the peg to tighten
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is not attached to the peg and the gripper is open, move
    # the gripper near the wrench and close it around the wrench.
    if check("the wrench is not attached to the peg and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is around the wrench, slide it down to the peg.
    if check("the wrench is attached to the peg and the robot's gripper is vertically aligned with the peg"):
        robot.move_gripper("left of the peg")
    # If the gripper is next to the peg, move it around the peg to tighten.  
    if check("the robot's gripper is above the peg and the wrench is wrapped around the peg"):
        robot.move_gripper("around the peg")