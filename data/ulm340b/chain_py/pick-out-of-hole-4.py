
    # Steps:
    #  1. Move the gripper near the peg
    #  2. Close the gripper around the peg
    #  3. Move the peg to the target location
    # If the gripper is near the peg, we can just close the gripper around it.
    if check("the robot's gripper is not near peg"):
        robot.place("gripper near peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near peg and the robot's gripper is closed"):
        robot.place("peg at goal")

# insert-peg-side: grab the peg and insert it into the hole from the side
def insert_peg_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg