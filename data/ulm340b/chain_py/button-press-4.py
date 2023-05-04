
    # Steps:
    #  1. Put gripper right of the button
    #  2. Start pushing the button in
    #  3. Push the button in harder
    # If the robot's gripper is not right of the button, move it there.
    if check("the robot's gripper is not right of button"):
        robot.move("gripper to right of button")
    # If the button is in front of the robot's gripper, we should start pushing
    # it in to press it.
    if check("button is in front of the robot's gripper"):
        robot.push("button in")
    # If the robot's gripper is starting to be past the button, push harder.
    if check("the robot's gripper is past button"):
        robot.push("button in harder")

# peg-insert-front: insert the peg into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg forwards into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the front, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# slider-pull: pull the slider open
def slider_pull(robot):
    # Steps:
    #  1. Put gripper on the