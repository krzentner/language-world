
    # Steps:
    #  1. Put gripper around peg
    #  2. Close gripper around peg
    #  3. Pull peg out of hole
    #  4. Move peg to goal
    # If the peg is not around the gripper, put it around the gripper.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.put("gripper around peg")
    # If the gripper is around the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If we closed the gripper, and the peg is still around the gripper, maybe
    # we grabbed it.
    # If the peg isn't in the hole, try to move it to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move("peg to goal")
    # If we closed the gripper, and the peg is still around the gripper, maybe
    # we grabbed it.
    # Try to pull it out of the hole by moving up.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.pull("peg out of hole")

# pick-place-hole: pick up the puck and drop it in the hole
def pick_place_hole(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Put puck above hole
    #  5. Drop puck in hole
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper