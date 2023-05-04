
    # Steps:
    #  1. Put gripper around edge of plate
    #  2. Push plate to goal
    # The robot can push the plate by holding the edge of the plate with the
    # gripper.
    # Put the gripper around the plate's edge, from the front of the plate.
    # Because the plate is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not forward aligned with the plate and the robot's gripper is not around the edge of plate"):
        robot.grab("the edge of plate")
    # Once the gripper is around the plate's edge, the plate should be between
    # the gripper.
    # The robot can push the plate to the target location.
    if check("the robot's gripper is forward aligned with plate and the robot's gripper is around the edge of plate"):
        robot.slide("plate to goal")

# pick-place-topdown: pick up the puck and hold it at the target location
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Close gripper around puck
    #  3. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is near the puck, maybe we can grab it by closing the
    # gripper.
    if check("the robot's gripper is above puck"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# peg-unstack-side: pull the top peg off the tower from the side
def peg_unstack_side