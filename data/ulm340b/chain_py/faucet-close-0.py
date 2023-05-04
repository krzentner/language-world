
    # Steps:
    #  1. Put gripper right of the faucet
    #  2. Push the faucet closed
    # If the gripper is not above the faucet, we should move the gripper above
    # the faucet.
    if check("the robot's gripper is not above the faucet"):
        robot.move("gripper above faucet")
    # Now, push the faucet closed.
    if check("the robot's gripper is above the faucet"):
        robot.push("the faucet closed")

# pick-place-side: grab the puck from the side and hold it at the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
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
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3