
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move lid to box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # Once the gripper is around the box lid, we can close the gripper to grab
    # the box lid.
    if check("the robot's gripper is above the box lid and the robot's gripper is not around box lid"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # If the gripper is open around the box lid, we can close it to pick up the
    # box lid.
    if check("the robot's gripper is closed"):
        robot.move_gripper("near the box")

# pick-place-wall: pick up the puck and place it next to the wall
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
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("above the wall")

# peg-insert-side-wall: grab the peg and insert it into the hole from the side
def peg_insert_side_wall(robot):