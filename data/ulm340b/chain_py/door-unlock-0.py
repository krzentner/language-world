
    # Steps:
    #  1. Put gripper above lock dial
    #  2. Drop gripper around lock dial
    #  3. Start twisting the lock dial
    #  4. Twist the lock dial harder
    # The robot's gripper can't grip the lock dial from the front, so we have to
    # move it vertically above it before trying to grab it.
    if check("the robot's gripper is not vertically aligned with lock dial"):
        robot.place("gripper above lock dial")
    # Since we just moved the gripper vertically, it's not around the lock dial
    # yet, so put it around the lock dial.
    if check("the robot's gripper is not around lock dial"):
        robot.place("gripper around lock dial")
    # If the gripper is still aligned with the lock dial vertically, keep trying
    # to turn it.
    if check("the robot's gripper is vertically aligned with lock dial and the robot's gripper is around lock dial"):
        robot.twist("lock dial")
    # The lock dial turned, so twist it harder.
    if check("the robot's gripper is almost vertically aligned with lock dial and the robot's gripper is around lock dial"):
        robot.twist("lock dial harder")

# peg-insert-back: grab the peg and insert it into the hole from the back
def peg_insert_back(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole from the back
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
  