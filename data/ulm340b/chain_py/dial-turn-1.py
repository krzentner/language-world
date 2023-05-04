
    # Steps:
    #  1. Put gripper above the dial
    #  2. Move the gripper down to the dial
    #  3. Turn the dial
    # The dial isn't that big, so first move the gripper down to be around the
    # dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper near dial")
    # Now that the gripper is near the dial, it should be easy to grab it
    if check("the robot's gripper is near the dial"):
        robot.grab("dial")
    # Once we grab the dial, we should be able to turn it by moving the gripper
    # left or right.
    if check("the robot's gripper is around dial"):
        robot.turn("dial counterclockwise")

# peg-insert-side-v1: move the peg sideways into the hole
def peg_insert_side_v1(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with peg and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("