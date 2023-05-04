
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Align gripper with goal
    #  5. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # Align the gripper with the goal so that we're moving the puck in the right
    # direction.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.align("the gripper with the goal")
    # Now that the gripper is aligned with the goal, move the puck to the goal.
    # We don't need to check if we're holding the puck, because even if we're
    # not, we just go back to trying to pick it up.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("puck to goal")

# hand-insert-side: pick up the peg and insert it into the target hole
def hand_insert_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Align peg to hole
    #  5. Move peg into hole
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's