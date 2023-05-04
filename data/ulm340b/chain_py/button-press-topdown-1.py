
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper into button to press button
    # The button can be pressed from above by pushing down on it with the robot's
    # gripper.
    # If the button isn't below the gripper as seen from above, move the gripper
    # above the button.
    if check("the robot's gripper is not above button and the robot's gripper is not vertically aligned with button"):
        robot.put("the gripper above the button")
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to push it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near button"):
        robot.push("the gripper into the button")

# peg-insert-front: grab the peg and insert it into the hole by pushing forward
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg straight into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with the hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the front, insert it.
    if check("the peg is vertically