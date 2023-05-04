
    # Steps:
    #  1. Move the gripper around the wall
    #  2. Move the gripper to the target
    # First, move the gripper around the wall.
    if check("the robot's gripper is not around the wall"):
        robot.move_gripper("around the wall")
    # Once the gripper is around the wall, just reach to the target.
    if check("the robot's gripper is around the wall"):
        robot.move_gripper("near the reach target")

# peg-insert-side-wall: grab the peg from behind the wall and insert it into the hole
def peg_insert_side_wall(robot):
    # Steps:
    #  1. Put gripper around the wall
    #  2. Move the gripper above the peg
    #  3. Line the peg up with the hole
    #  4. Slide the peg into the hole
    # First, move the robot's gripper around the wall.
    if check("the robot's gripper is not around the wall"):
        robot.move_gripper("around the wall")
    # Then, move the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper is not aligned with the peg, we can line it up.
    if check("the peg is not left of the robot's gripper and the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the peg is not right of the robot's gripper and the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.move_gripper("almost vertically aligned with the peg")
    # If the peg is mostly lined up with the hole to the side, insert it.
    if check("the peg is almost horizontally aligned with hole"):
        robot.move_gripper("above the peg")

# drawer-open-wall: pull the drawer open without hitting the wall
def drawer_open_wall(robot):
   