
    # Steps:
    #  1. Reach towards the target
    # This is similar to "reach". Because the wall is short, we just need to go
    # around it.
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")

# peg-insert-topdown: line up the peg with the hole and insert the peg into the hole
def peg_insert_topdown(robot):
    # Steps:
    #  1. Move the peg above the hole
    #  2. Line up the peg with the hole
    #  3. Drop the peg down into the hole
    #  4. Let go of the peg
    # First, move the peg above the hole.
    if check("the peg is not below the robot's gripper"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is lined up with the hole, try to drop it in the hole.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("almost vertically aligned with hole")
    # If the peg is above the hole, drop the peg down into the hole.
    if check("the peg is below the robot's gripper"):
        robot.move_gripper("almost horizontally aligned with hole")
    # Finally, let go of the peg.
    if check("the peg is horizontally aligned with hole and peg is almost below the robot's gripper"):
        robot.move_gripper("horizontally aligned with hole")

# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the