
    # Steps:
    #  1. Put gripper to the right of the button
    #  2. Start pushing the button from the front
    #  3. Push button in harder
    # First, make sure that the robot's gripper is at the same height as the
    # button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Put the gripper to the right of the button to push on it.
    if check("the robot's gripper is not to the right of button"):
        robot.put("gripper to the right of button")
    # Push the button from the front, towards the robot.
    # We can only do this if the gripper is roughly to the right of the button.
    if check("the robot's gripper is to the right of button"):
        robot.push("button forward")
    # If we managed to line up the gripper to the right of the button, just push
    # it harder to try to press the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button forward harder")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper right of the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole
    # First, put the gripper right of the peg.
    if check("the robot's gripper is not left of the peg and the robot's gripper is not horizontally aligned with peg"):
        robot.put("gripper right of peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # right of the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not horizontally aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still roughly horizontally aligned with the peg,
