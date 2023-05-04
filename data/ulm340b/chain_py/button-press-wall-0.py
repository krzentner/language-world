
    # Steps:
    #  1. Line up the gripper from in front
    #  2. Push the button down
    # Move the gripper so it's in front of the button.
    if check("the robot's gripper is not in front of button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is in front of button"):
        robot.push("the button down")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper")