
    # Steps:
    #  1. Put gripper above peg
    #  2. Move gripper down around the peg
    #  3. Slide gripper forward into hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    # If the gripper is vertically aligned with the peg, we can try to move it
    # near the peg.
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not near peg"):
        robot.move("gripper to peg")
    # If the gripper is near the peg, we can try to move it forward into the
    # hole.
    if check("the robot's gripper is near peg and the peg is near hole"):
        robot.push("gripper into hole")

# peg-unplug-side: grab the peg and unplug it from the hole from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Move gripper down around the peg
    #  3. Slide gripper backwards out of hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    # If the gripper is vertically aligned with the peg, we can try to move it
    # near the peg.
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not near peg"):
        robot.move("gripper to peg")
    # If the gripper is near the peg, we can try to move it backward out of the
    # hole.
    if check("the robot's gripper is near peg and the peg is near hole"):
        robot.slide("gripper out of hole")

# pick-place-wall: pick up the object and hold it on the target spot on the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Line up gripper above peg
    #  2. Move gripper around peg
    #  3. Pick peg up and move gripper to wall
    #  