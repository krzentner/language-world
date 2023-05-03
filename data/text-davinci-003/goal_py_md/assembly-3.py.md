

The robot should use its gripper to grab the wrench and wrap it around the peg.

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench so it wraps around the peg
    #  4. Rotate the wrench so that it catches the peg
    
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is not below the gripper, move the gripper above it.
    if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is not above the wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # If the gripper is near the wrench, move the gripper so that it can wrap 
    # around the peg.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.move_gripper("above the peg")
    # Once the gripper is above the peg, we can rotate the wrench to catch the 
    # peg.
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the peg")