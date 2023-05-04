
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift up gripper
    #  5. Put gripper above target bin
    #  6. Drop gripper into bin
    #  7. Open gripper
    # First, put the gripper roughly above cube.
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Now lift up the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.raise("gripper above cube")
    # Now that we have the cube, put it above the target bin.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("gripper above target bin")
    # The gripper is already near the target bin, so drop the cube into it.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.drop("gripper into target bin")
    # Finally, open the gripper.
    if check("the robot's gripper is closed"):
        robot.open("gripper")

# peg-unstack: lift the top peg up from the stack of pegs
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above top peg
    #  2. Drop gripper around top peg
    #  3. Close gripper around top peg
 