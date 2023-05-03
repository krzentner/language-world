# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper around the peg and wrench
    #  4. Let go of the wrench
    #  5. Pick up the peg and wrench together
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the wrench is not within the gripper's reach, move the gripper closer to it.
    if check("the robot's gripper is not near the wrench"):
        robot.reach("towards wrench")
    # When the wrench is within the gripper's reach, grab it.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # Position the gripper above the peg, with the wrench around the peg.
    if check("the robot's gripper is not above the peg and wrench and the wrench is grabbed"):
        robot.put("gripper above peg and wrench")
    # Let go of the wrench.
    if check("the wrench is in the gripper and the gripper is around the peg and wrench"):
        robot.release("wrench")
    # Pick up the peg and wrench together.
    if check("the gripper is above the peg and wrench and the wrench is released"):
        robot.grab("peg and wrench")