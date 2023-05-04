
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Lift gripper and slide to hole
    #  4. Move gripper horizontally to drop peg in
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg", close_gripper=True)
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("around peg", close_gripper=True)
    # If the gripper is around the peg, we can lift it.
    if check("the robot's gripper is around peg and the robot's gripper is not vertically aligned with hole"):
        robot.move_gripper("vertically aligned with hole")
    # If the gripper is above the hole, we should be able to slide the peg in
    # from the side.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("horizontally aligned with hole")

# door-lock: insert the key in the lock
def door_lock(robot):
    # Steps:
    #  1. Put gripper above key
    #  2. Drop gripper around key
    #  3. Lift gripper and slide to hole
    #  4. Move gripper horizontally to insert key in
    # First, put the gripper roughly above key, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above key"):
        robot.move_gripper("above key", close_gripper=True)
    # If the gripper isn't around the key, put it around the key.
    if check("the robot's gripper is not around key and the robot's gripper is open"):
        robot.move_gripper("around key", close_gripper=True)
    # If the gripper is around the key, we can lift it.
    if check("the robot's grip