
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Grab the peg
    #  4. Move peg above hole
    #  5. Put peg in hole
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg, close it to try to grab the peg.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.grab("the peg")
    # If the gripper is above the peg and the peg is still there, move the gripper
    # with the peg above the hole.
    if check("the robot's gripper is above peg and the peg is near the robot's gripper"):
        robot.lift("the peg above the hole")
    # If the gripper is above the hole, we can put the peg in.
    if check("the robot's gripper is above the hole and the peg is in front of the robot's gripper"):
        robot.place("the peg into the hole")

# peg-insert-side-long: grab the peg and insert it into the hole from the side
# with a long peg
def peg_insert_side_long(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Grab the peg
    #  4. Move peg above hole
    #  5. Put peg in hole
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg