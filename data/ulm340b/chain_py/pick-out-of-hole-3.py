
    # Steps:
    #  1. Put gripper above the peg
    #  2. Move gripper down until it's around the peg
    #  3. Pull the peg out
    #  4. Move puck to goal
    # First, put the gripper above the peg to pick it out of the hole.
    # This makes sure we don't bump the peg accidentally.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # If the gripper is above the peg but not around it, move the gripper down
    # around the peg to pick it up.
    if check("the robot's gripper is above the peg and the robot's gripper is not near peg"):
        robot.place("gripper around peg")
    # If the gripper is near the peg, we probably grabbed it.
    # Pull the peg out.
    if check("the robot's gripper is near peg"):
        robot.pull("peg out of the hole")
    # We grabbed the peg out of the hole, and it's still below the gripper.
    # Move the puck to the goal.
    # If we didn't actually grab the peg, we'll just go back to an earlier step.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-from-hole: pick the peg out of the hole and place it on the table at the goal
def pick_place_from_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Move gripper down until it's around the peg
    #  3. Pull the peg out
    #  4. Move peg to goal
    #  5. Open gripper to drop peg
    # First, put the gripper above the peg to pick it out of the hole.
    # This makes sure we don't bump the peg accidentally.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # If the gripper is above the peg but not around it, move the gripper down
    # around the peg to pick it