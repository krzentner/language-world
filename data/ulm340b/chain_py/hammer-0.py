
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Put gripper above nail
    #  3. Push down on nail from above
    # Because this is "topdown", we just need to line up the gripper from above.
    # First, line the gripper up above the nail.
    # If the hammer is not above the nail, move it.
    if check("the hammer is not vertically aligned with the nail"):
        robot.put("gripper above nail")
    # Now that the hammer is lined up, just push down on the nail.
    if check("the robot's gripper is above nail"):
        robot.push("down on nail")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg into the hole
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole, push it into the hole.
    if check("peg is horizontally aligned with hole"):
        robot